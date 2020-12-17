from appl import db
from appl.models import User, Blog


def test_moderation():
    db.create_all()
    user1 = User(name='test123', username='test1',
                 email='test1@g.com', password='test123')
    blog1 = Blog(title='Artificial intelligence', intro='Artificial\
                intelligence, is intelligence\
                demonstrated by machines, unlike the natural\
                intelligence displayed by humans and\
                animals.', content='Artificial intelligence (AI)\
                is wide-ranging branch of computer\
                science concerned with building smart machines\
                capable of performing tasks that\
                typically require human intelligence. AI is\
                an interdisciplinary science with\
                multiple approaches, but advancements in machine\
                learning and deep learning\
                are creating a paradigm shift in virtually every\
                sector of the tech industry.\
                Less than a decade after breaking the Nazi encryption\
                machine Enigma and\
                helping the Allied Forces win World War II,\
                mathematician Alan Turing changed\
                history a second time with a simple question:\
                "Can machines think?" Turing paper\
                "Computing Machinery and Intelligence" (1950),\
                and its subsequent Turing Test,\
                established the fundamental goal and vision of\
                artificial intelligence. At its\
                core, AI is the branch of computer science that\
                aims to answer Turings question\
                in the affirmative. It is the endeavor to replicate\
                or simulate human intelligence\
                in machines.', user_id=1)

    blog2 = Blog(title='Artificial intelligence', intro='Artificial\
                intelligence, is intelligence\
                demonstrated by machines, unlike the natural\
                intelligence displayed by humans and\
                animals.', content='Artificial intelligence (AI)\
                is wide-ranging branch of computer\
                science concerned with building smart machines\
                capable of performing tasks that\
                typically require human intelligence. AI is\
                an interdisciplinary science with\
                multiple approaches, but advancements in machine\
                learning and deep learning\
                are creating a paradigm shift in virtually every\
                sector of the tech industry.\
                Less than a decade after breaking the Nazi encryption\
                machine Enigma and\
                helping the Allied Forces win World War II,\
                mathematician Alan Turing changed\
                history a second time with a simple question:\
                "Can machines think?" Turing paper\
                "Computing Machinery and Intelligence" (1950),\
                and its subsequent Turing Test,\
                established the fundamental goal and vision of\
                artificial intelligence. At its\
                core, AI is the branch of computer science that\
                aims to answer Turings question\
                in the affirmative. It is the endeavor to replicate\
                or simulate human intelligence\
                in machines.', user_id=1)

    blog3 = Blog(title='Artificial intelligence', intro='Artificial\
                intelligence, is intelligence\
                demonstrated by machines, unlike the natural\
                intelligence displayed by humans and\
                animals.', content='Artificial intelligence (AI)\
                is wide-ranging branch of computer\
                science concerned with building smart machines\
                capable of performing tasks that\
                typically require human intelligence. AI is\
                an interdisciplinary science with\
                multiple approaches, but advancements in machine\
                learning and deep learning\
                are creating a paradigm shift in virtually every\
                sector of the tech industry.\
                Less than a decade after breaking the Nazi encryption\
                machine Enigma and\
                helping the Allied Forces win World War II,\
                mathematician Alan Turing changed\
                history a second time with a simple question:\
                "Can machines think?" Turing paper\
                "Computing Machinery and Intelligence" (1950),\
                and its subsequent Turing Test,\
                established the fundamental goal and vision of\
                artificial intelligence. At its\
                core, AI is the branch of computer science that\
                aims to answer Turings question\
                in the affirmative. It is the endeavor to replicate\
                or simulate human intelligence\
                in machines.', user_id=1)

    db.session.add_all([user1, blog1, blog2, blog3])
    db.session.commit()


if __name__ == "__main__":
    test_moderation()
