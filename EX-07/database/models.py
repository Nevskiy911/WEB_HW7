from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, event, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("cell_phone", String(120))
    address = Column(String(120))
    start_work = Column(Date, nullable=False)
    students = relationship(
        "Students", secondary="teachers_to_students", back_populates="teachers"
    )


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey(
        'teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column('date_of', Date, nullable=True)
    student_id = Column('student_id', ForeignKey(
        'students.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', ForeignKey(
        'disciplines.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grade')
    discipline = relationship('Discipline', backref='grade')
