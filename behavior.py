

class Behavior:



    def __init__(self, bbcon, sensobs, motor_recommendations, active_flag, halt_request, priority, match_degree, weight):
        """
        Init-klassen som instansierer følgende:
        :param bbcon:                 Controller-klassen som hører til denne handlingen hører til
        :param sensobs:               Cn liste med alle sensobs denne handlingen bruker
        :param motor_recommendations: En liste med andbefalinger, en per motob, som denne handlingen tilrettelegger til artbritratoren
        :param active_flag:           Boolean som indikerer om handlingen er aktiv eller ikke
        :param halt_request:          Boolean som sier hvorvidt roboten skal stoppe
        :param priority:              En statisk verdi som indikerer viktigheten til handlingen
        :param match_degree:          Et reelt tall fra 0 til 1 som indikerer verdien til handlingen gitt nåværende forhold
        :param weight:                Produktet av priority*match_degree som arbitrator for å velge vinnende handling
        """
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.motor_recommandation = motor_recommendations
        self.active_flag = active_flag
        self.halt_request = halt_request
        self.priority = priority
        self.match_degree = match_degree
        self.weight = weight

    def consider_deactivation(self):
        # TODO 1: Skrive metode som tester hvorvidt handlingen skal deaktiveres, dersom den er activ

    def consider_activation(self):
        # TODO 2: skrive metode som tester hvorvidt handlingen skal aktiveres, dersom den er deaktivert

    def update(self):
        # TODO 3: Skrive metode som oppdaterer aktivitetsstatusen

    def sense_and_act(self):
        # TODO 4: Skrive metode som for hver behavior ser på sensor dataen (values) og lager motob andbefalinger, og legger disse i sin egen liste med motob andbefalinger. Må også oppdatere match_degree basert på dataen, og oppdatere sin egen metch degree.







