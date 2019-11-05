"""Behavior klassen"""


class Behavior:
    """Behavior klassen"""

    def __init__(self, bbcon, active_flag, priority, sensobs=None, halt_request=False):
        """
        :param sensobs: Én eller flere sensobs.
        """
        self.sensobs = sensobs
        self.bbcon = bbcon
        self.active_flag = active_flag
        self.priority = priority
        self.halt_request = halt_request
        self.match_degree = 0
        self.weight = 0
        self.motor_recommendations = None

    def consider_deactivation(self):
        """Sjekker om den burde deaktiveres"""
        pass

    def consider_activation(self):
        """Sjekker om den burde aktiveres igjen."""
        pass

    def update(self):
        """Update"""

        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sensobs[0].update()
            recommendation, match_degree = self.sense_and_act()
            self.weight = match_degree * self.priority
            self.motor_recommendations = recommendation
        else:
            self.weight = 0

    def sense_and_act(self):
        """Lager motob-anbefalinger basert på verdier fra sine sensobs."""
        return "empty recommendation", 0


class CarryOn(Behavior):
    """
    Går videre
    """

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def sense_and_act(self):
        """
        Sense and act
        :return (recommendation, match_degree)
        """
        return "forward", 1


class AvoidLines(Behavior):
    """
    Går videre
    Alltid aktiv, trenger ikke
    """

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def sense_and_act(self):
        """
        Sense and act
        :return (recommendation, match_degree)
        """
        line_detection = []
        for sensob in self.sensobs:
            line_detection.append(sensob.value)

        match_degree = 0

        recommendation = "adjust right" if line_detection[0] else "forward"
        recommendation = "adjust left" if line_detection[2] else recommendation
        recommendation = "stop" if line_detection[1] or (line_detection[0] and line_detection[2]) else recommendation

        match_degree = 1 if line_detection[0] or line_detection[1] or line_detection[2] else match_degree

        return recommendation, match_degree


class Obstacle(Behavior):

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def sense_and_act(self):
        distance = self.sensobs.value

        recommendation, match_degree = "forward", 0.1

        if distance < 20:
            recommendation = "stop"
            match_degree = (20 - distance) / 10

        return recommendation, match_degree


class Picture(Behavior):

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def sense_and_act(self):
        pic_val = self.sensobs.value

        recommendation= "forward"
        match_degree = 0.1

        if pic_val[2] > 0.7:
            recommendation = "forward"
            match_degree = 1
        else:
            recommendation = "turn around"
            match_degree = 1

        return recommendation, match_degree






























