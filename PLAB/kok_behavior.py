import math

class Behavior:
    """Behavior-klassen"""

    def __init__(self, bbcon, sensobs=None):
        """
        Init-metoden som instansierer følgende:
        :param bbcon:                 Controller-klassen som hører til denne handlingen hører til
        :param sensobs:               En liste med alle sensobs denne handlingen bruker i rekkefølge: [kamera, ultrasonic, ir]
        :param motor_recommendations: En liste med andbefalinger, en per motob, som denne handlingen tilrettelegger til artbritratoren
        :param active_flag:           Boolean som indikerer om handlingen er aktiv eller ikke
        :param halt_request:          Boolean som sier hvorvidt roboten skal stoppe
        :param priority:              En statisk verdi som indikerer viktigheten til handlingen
        :param match_degree:          Et reelt tall fra 0 til 1 som indikerer verdien til handlingen gitt nåværende forhold
        """
        if not isinstance(sensobs, list) or not isinstance(motor_recommendations, list):
            print("The parameters sensobs and motor_recommendations must be lists")

        self.bbcon = bbcon
        self.sensobs = sensobs #[kamera,utrsonic,ir]
        self.motor_recommendations = None
        self.active_flag = False
        self.halt = False
        self.priority = 1
        self.match_degree = 0
        self.weight = self.priority * self.match_degree

    def halt_request(self, halter):
        self.halt = halter
        if halter:
            self.active_flag = halter

    def reset(self):
        """Resetter match_degree og motor_recommendations"""
        self.match_degree = 0
        self.motor_recommendations = None

    def consider_activation(self):
        """Sjekker om den skal akriveres"""
        self.active_flag = True

    def consider_deactivation(self):
        """Sjekker om den skal akriveres"""
        self.active_flag = True

    def sense_and_act(self):
        """Abstrakt metode"""
        return

    def update(self):
        """
        Kalles hvert timestep
        """
        if self.active_flag:
            self.consider_deactivation()
            self.sense_and_act()
        else:
            self.consider_activation()

        self.weight = self.priority * self.match_degree

class Go(Behavior):
    """Go-behavior"""

    def __init__(self, bbcon):
        """Init"""
        super().__init__(bbcon)
        self.priority = bbcon.behavior_values["go_pri"]

    def sense_and_act(self):
        """Senser og acter :--)"""
        # TODO: koke denne ferdig, bbcon må skrives bedre
        self.reset()


class AvoidCollision(Behavior):
    """Unngår kollisjoner"""

    def __init__(self, bbcon, ultra_sonic):
        """Init"""
        super().__init__(bbcon, [ultra_sonic])
        self.priority = bbcon.behavior_values["avcol_pri"]

    def sense_and_act(self):
        dist = self.sensobs[0].get_value()
        min_dist = self.bbcon.behavior_values["min_dist"]
        self.reset()

        if dist > min_dist:
            self.motor_recommendations = self.bbcon.behavior_values["back"]
            self.match_degree = 1


class AvoidWhiteLine(Behavior):
    """Unngår hvit linje"""
    def __init__(self, bbcon, ir_sensor):
        """Init"""
        super().__init__(bbcon, [ir_sensor])
        self.priority = bbcon.behavior_values["avline_pri"]

    def consider_activation(self):
        """Sjekker om den skal akriveres"""
        self.active_flag = True

    def consider_deactivation(self):
        """Sjekker om den skal akriveres"""
        self.active_flag = False

    def sense_and_act(self):
        """Sjekker om den er over en hvit linje"""
        ir_values = self.sensobs[0].get_value()
        tresh = self.bbcon.behavior_values["white_tresh"]
        self.reset()
        average = math.fsum(ir_values) / len(ir_values)
        if average < tresh:
            self.motor_recommendations = self.bbcon.behavior_values["turn"]
            self.match_degree = 1


class Stop(Behavior):
    """Stopper"""
    def __init__(self, bbcon, cam_sensor):
        """Init"""
        super().__init__(bbcon, [cam_sensor])
        self.priority = bbcon.behavior_values["cam_pri"]
        self.stopped = False

    def consider_activation(self):
        """Sjekker om den skal akriveres"""
        self.active_flag = True

    def consider_deactivation(self):
        """Sjekker om den skal akriveres"""
        if self.halt:
            self.active_flag = False

    def sense_and_act(self):
        """Tar bilde av hva enn som står foran"""
        img = self.sensobs[0].get_value()
        blue_tresh = self.bbcon.behavior_values["blue_tresh"]
        self.reset()

        if self.stopped and img[2] > blue_tresh:
            self.motor_recommendations = self.bbcon.behavior_values["forward"]
            self.stopped = False
        elif img[2] >

