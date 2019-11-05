"""Behavior klassen"""


class Behavior:
    """Behavior klassen"""

    def __init__(self, bbcon, active_flag, priority, sensobs, halt_request=False):
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
            for sensob in self.sensobs:
                sensob.update()
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

    def __init__(self, bbcon, active_flag, priority, sensobs):
        super().__init__(bbcon, active_flag, priority, sensobs)

    def consider_deactivation(self):
        if self.bbcon.motob.recommendation is "investigate":
            print("Deactivating " + self.__class__.__name__)
            self.active_flag = False

    def consider_activation(self):
        if self.bbcon.motob.recommendation is "bull rage" or "turn around":
            print("Activating " + self.__class__.__name__)
            self.active_flag = True

    def sense_and_act(self):
        """
        Sense and act
        :return (recommendation, match_degree)
        """
        distance = self.sensobs[0].value

        recommendation, match_degree = "forward", .5
        if distance < self.bbcon.config_values["distance_tresh"]:
            recommendation, match_degree = "investigate", 3

        return recommendation, match_degree


class AvoidLines(Behavior):
    """
    Går videre
    Alltid aktiv, trenger ikke
    """

    def __init__(self, bbcon, active_flag, priority, sensobs):
        super().__init__(bbcon, active_flag, priority, sensobs)

    def consider_deactivation(self):
        if self.bbcon.motob.recommendation is "investigate":
            print("Deactivating " + self.__class__.__name__)
            self.active_flag = False

    def consider_activation(self):
        if self.bbcon.motob.recommendation is "bull rage" or "turn around":
            print("Activating " + self.__class__.__name__)
            self.active_flag = True

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

        if self.bbcon.rages is 3:
            self.halt_request = True
            match_degree = 100

        return recommendation, match_degree


# class Obstacle(Behavior):
#
#     def __init__(self, bbcon, active_flag, priority, sensobs):
#         super().__init__(bbcon, active_flag, priority, sensobs)
#
#     def sense_and_act(self):
#         distance = self.sensobs.value
#
#         recommendation, match_degree = "forward", 0.1
#
#         if distance < 20:
#             recommendation = "stop"
#             match_degree = (20 - distance) / 10
#
#         return recommendation, match_degree


class Picture(Behavior):

    def __init__(self, bbcon, active_flag, priority, sensobs):
        super().__init__(bbcon, active_flag, priority, sensobs)

    def consider_deactivation(self):
        if self.bbcon.motob.recommendation is "bull rage" or "turn around":
            print("Deactivating " + self.__class__.__name__)
            self.active_flag = False

    def consider_activation(self):
        if self.bbcon.motob.recommendation is "investigate":
            print("Activating " + self.__class__.__name__)
            self.active_flag = True

    def sense_and_act(self):
        pic_val = self.sensobs[0].value

        if pic_val[2] > self.bbcon.config_values["blue_tresh"]:
            self.bbcon.rages += 1
            recommendation = "bull rage"
            match_degree = 1
        else:
            recommendation = "turn around"
            match_degree = 1

        self.sensobs[0].sensors[0].reset()

        return recommendation, match_degree






























