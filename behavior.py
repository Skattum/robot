

class Behavior:



    def __init__(self, bbcon, sensobs, motor_recommendations, active_flag, halt_request, priority, match_degree, weight):
        """

        :param bbcon: controller-klassen som hører til denne behavior hører til
        :param sensobs: en liste med alle sensobs denne behavior bruker
        :param motor_recommendations:
        :param active_flag:
        :param halt_request:
        :param priority:
        :param match_degree:
        :param weight:
        """
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.motor_recommandation = motor_recommendations
        self.active_flag = active_flag
        self.halt_request = halt_request
        self.priority = priority
        self.match_degree = match_degree
        self.weight = weight






