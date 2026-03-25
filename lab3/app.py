from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Course
from repositories import SQLAlchemyCourseRepository

app = Flask(__name__)

# Database Setup (from Lab 2)
engine = create_engine('sqlite:///edx_platform.db')
session_factory = scoped_session(sessionmaker(bind=engine))
repo = SQLAlchemyCourseRepository(session_factory)

# Ensure tables exist
Base.metadata.create_all(engine)

@app.route('/')
def index():
    # Requirement 5 & 6: Fetching data via Business Logic/Repository level
    session = session_factory()
    courses = session.query(Course).all()
    return render_template('index.html', courses=courses)

@app.route('/add', methods=['POST'])
def add_course():
    # Requirement 4: Create functionality
    course_id = request.form.get('course_id')
    title = request.form.get('title')
    price = float(request.form.get('price'))
    
    new_course = Course(course_id=course_id, title=title, price=price)
    
    session = session_factory()
    session.add(new_course)
    session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_course(id):
    # Requirement 4: Delete functionality
    session = session_factory()
    course = session.query(Course).get(id)
    if course:
        session.delete(course)
        session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)