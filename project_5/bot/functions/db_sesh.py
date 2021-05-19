from databases.db_engine import User, Interview, session

class EditDB:
    def __init__(self, data):
        self.user_id = data.from_user.id
        self.username = data.from_user.mention
        if self.sesh() != None:
            self.__username_updater()

    def __counter(self):
        ed_usr = self.sesh()
        if self.count_value == 'add':
            ed_usr.count += 1
        elif self.count_value == 'last':
            ed_usr.count -= 1
        elif self.count_value == 'all':
            ed_usr.count = 0
        session.commit()

    def __username_updater(self):
        ed_usr = self.sesh()
        if ed_usr.username != self.username:
            self.edit_user({'username': self.username})

    def sesh(self):
        user = session.query(User).filter_by(user_id=self.user_id).first()
        return user

    def add_new_user(self):
        user = User(
            username = self.username,
            user_id = self.user_id,
            )
        session.add(user)
        session.commit()

    def add_observ(self):
        self.count_value = 'add'
        self.__counter()
        ed_usr = self.sesh()
        observ = Interview(
            db_id=ed_usr.id,
            question_1=ed_usr.question_1, question_2=ed_usr.question_2, question_3=ed_usr.question_3,
            question_4=ed_usr.question_4, question_5=ed_usr.question_5, question_6=ed_usr.question_6,
            question_7=ed_usr.question_7, question_8=ed_usr.question_8, question_9=ed_usr.question_9,
            question_10=ed_usr.question_10, question_11=ed_usr.question_11, question_12=ed_usr.question_12,
            question_13=ed_usr.question_13, question_14=ed_usr.question_14, question_15=ed_usr.question_15,
            question_16=ed_usr.question_16, question_17=ed_usr.question_17, question_18=ed_usr.question_18,
            question_19=ed_usr.question_19, question_20=ed_usr.question_20, question_21=ed_usr.question_21,
            question_22=ed_usr.question_22
        )
        session.add(observ)
        session.commit()

    def del_observ(self, count_value):
        if count_value not in ['all', 'last']:
            return
        self.count_value = count_value
        ed_usr = self.sesh()
        if ed_usr.count != 0:
            observs = session.query(Interview).filter_by(db_id=ed_usr.id).all()
            if count_value == 'all':
                for obsrv in observs:
                    observ = session.query(Interview).filter_by(db_id=ed_usr.id).first()
                    session.delete(observ)
                    session.commit()
            elif count_value == 'last':
                last_observ = observs[-1]
                session.delete(last_observ)
                session.commit()
            self.__counter()

    def edit_user(self, param_dict):
        ed_usr = self.sesh()
        for par in param_dict:
            if par == 'username':
                ed_usr.username = param_dict[par]
            elif par == 'status':
                ed_usr.status = param_dict[par]
            elif par == 'message_id':
                ed_usr.message_id = param_dict[par]
            elif par == 'message_id_2':
                ed_usr.message_id_2 = param_dict[par]
            elif par == 'question_1':
                ed_usr.question_1 = param_dict[par]
            elif par == 'question_2':
                ed_usr.question_2 = param_dict[par]
            elif par == 'question_3':
                ed_usr.question_3 = param_dict[par]
            elif par == 'question_4':
                ed_usr.question_4 = param_dict[par]
            elif par == 'question_5':
                ed_usr.question_5 = param_dict[par]
            elif par == 'question_6':
                ed_usr.question_6 = param_dict[par]
            elif par == 'question_7':
                ed_usr.question_7 = param_dict[par]
            elif par == 'question_8':
                ed_usr.question_8 = param_dict[par]
            elif par == 'question_9':
                ed_usr.question_9 = param_dict[par]
            elif par == 'question_10':
                ed_usr.question_10 = param_dict[par]
            elif par == 'question_11':
                ed_usr.question_11 = param_dict[par]
            elif par == 'question_12':
                ed_usr.question_12 = param_dict[par]
            elif par == 'question_13':
                ed_usr.question_13 = param_dict[par]
            elif par == 'question_14':
                ed_usr.question_14 = param_dict[par]
            elif par == 'question_15':
                ed_usr.question_15 = param_dict[par]
            elif par == 'question_16':
                ed_usr.question_16 = param_dict[par]
            elif par == 'question_17':
                ed_usr.question_17 = param_dict[par]
            elif par == 'question_18':
                ed_usr.question_18 = param_dict[par]
            elif par == 'question_19':
                ed_usr.question_19 = param_dict[par]
            elif par == 'question_20':
                ed_usr.question_20 = param_dict[par]
            elif par == 'question_21':
                ed_usr.question_21 = param_dict[par]
            elif par == 'question_22':
                ed_usr.question_22 = param_dict[par]
            session.commit()