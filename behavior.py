"""Behavior klassen"""


class Behavior:
    """Behavior klassen"""

    def __init__(self, bbcon, sensobs, active_flag, priority, halt_request=False, match_degree=0):
        """
        :param sensobs: Én eller flere sensobs.
        """
        self.sensobs = list(sensobs)
        self.bbcon = bbcon
        self.active_flag = active_flag
        self.priority = priority
        self.halt_request = halt_request
        self.match_degree = match_degree
        self.weight = 0
        self.motor_recommendations = None

    def consider_deactivation(self):
        """Sjekker om den burde deaktiveres"""
        pass

    def consider_activation(self):
        """Sjekker om den burde aktiveres igjen."""
        pass

    def update(self):
        #   1. Kall testene om de må utføres.
        #   2. Kall på sense_and_act.
        pass

    def sense_and_act(self):
        """Lager motob-anbefalinger basert på verdier fra sine sensobs."""
        pass


class CarryOn(Behavior):
    """
    Går videre
    Alltid aktiv, trenger ikke
    """

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def update(self):
        """Update"""
        for sensob in self.sensobs:
            sensob.update()
        recommendation, match_degree = self.sense_and_act()
        self.weight = match_degree * self.priority
        self.motor_recommendations = recommendation

    def sense_and_act(self):
        """
        Sense and act
        :return (recommendation, match_degree)
        """
        line_detection = []
        for sensob in self.sensobs:
            line_detection.append(sensob.value)

        recommendation = "adjust right" if line_detection[0] else "forward"
        recommendation = "adjust left" if line_detection[2] else recommendation
        recommendation = "stop" if line_detection[1] or (line_detection[0] and line_detection[2]) else recommendation
        return recommendation, 1


class Obstacle(Behavior):

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def update(self):
        """Update"""

        self.sensobs[0].update()
        recommendation, match_degree = self.sense_and_act()
        self.weight = match_degree * self.priority
        self.motor_recommendations = recommendation

    def sense_and_act(self):

        distance = self.sensobs[0].value


        recommendation, match_degree = ("forward", 0.1)

        if distance < 0.07:
            recommendation = "stop"
            match_degree = 1


        return recommendation, match_degree

class Picture(Behavior):

    def __init__(self, bbcon, sensobs, active_flag, priority):
        super().__init__(bbcon, sensobs, active_flag, priority)

    def update(self):
        """Update"""

        self.sensobs[0].update()
        recommendation, match_degree = self.sense_and_act()
        self.weight = match_degree * self.priority
        self.motor_recommendations = recommendation


    def sense_and_act(self):

        pic_val = self.sensobs[0].value

        recommendation= "forward"
        match_degree = 0.1

        if pic_val[2] > 0.7:
            recommendation = "forward"
            match_degree = 1
        else:
            recommendation = "adjust left"
            match_degree = 1

        return recommendation, match_degree






























