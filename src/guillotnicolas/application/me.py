import curses
import time

height = 10


def slow_type(stdscr, text, typing_speed=0.05):
    global height
    header = ""
    lines = text.split('\n')
    total_lines = len(lines)
    displayed_lines = [""] * (height - 3)

    for current_line_index in range(total_lines):
        displayed_lines[current_line_index % (height - 3)] = ""
        current_line = lines[current_line_index]
        if not current_line:
            header = ""
            stdscr.addstr(height - 1, 0, "Press Enter to continue...")
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.move(height - 1, 0)
            stdscr.clrtoeol()
            if not header:
                header = current_line

        j = 0
        for char in current_line:
            displayed_lines[current_line_index % (height - 3)] = (
                    displayed_lines[current_line_index % (height - 3)] + char)
            for i in range(height - 3):
                stdscr.move(i, 0)
                stdscr.clrtoeol()
            for i in range(height - 3):
                stdscr.addstr(i, 0, displayed_lines[(current_line_index + i + 1) % (height - 3)])
            j += 1
            time.sleep(typing_speed)
            update_progress(stdscr, current_line_index + (j / len(current_line)), total_lines - 1, header)
            stdscr.refresh()


def update_progress(stdscr, current, total, header):
    global height
    bar_length = 40
    filled_length = int(bar_length * current // total)
    bar = '░' * filled_length + '-' * (bar_length - filled_length)

    stdscr.move(height, 0)
    stdscr.clrtoeol()
    stdscr.addstr(height, 0, f"|{bar}|  ~  {header}")


def cover_letter(stdscr):
    curses.curs_set(0)  # Cacher le curseur
    text = """ABOUT ME
--------
Introducing myself with a 'pip install' and a python package script feels like a pythonic way to apply for
your Python Tutorial Writer position. So here it is, briefly:
I'm Nicolas Guillot, 44 years old, married, and a father of three.
I live near Grenoble in the French Alps and enjoy mountain biking.

MY EXPERIENCE
-------------
I'm a software architect with 20 years in the industry.
I've worked as a developer, designer (UML, Figma), team leader, and architect in software and systems.
Focusing on Python, I’ve taught myself through personal projects, from standalone PyQT apps to web
applications using Django, Flask, FastAPI, and SQLAlchemy.
Recently, I’ve introduced Python as a primary development language in my company, emphasizing
speed of development, industrialization (best practices, CI, testing, IDE, Docker), and more.
I’ve trained my team and provided numerous tutorials and best practices on our internal Confluence.

MY MOTIVATION
-------------
In my daily work, I enjoy:
- Doing things the right way
- Sharing knowledge in a simple, pedagogical manner
- Coding in Python and learning new things
That's why I subscribed to your newsletter, and your offer truly resonates with me.

MY SKILLS
---------
I possess solid Python skills, but my greatest asset here is my ability to share and document concepts clearly.
I focus on structure: 5W1H—my writing always starts with What and Why. Once the target is clear,
the reader can grasp the How, and most importantly, its purpose.
Leonardo da Vinci once said, 'Simplicity is the ultimate sophistication,' and that's my mantra.

MY COMMITMENT
-------------
Will I dedicate enough time each week to Real Python?
I hope the way I've structured my cover letter demonstrates my commitment to this opportunity.

LET'S MEET ?
------------
I look forward to meeting you to discuss this opportunity.
You can find more about me in the attached resume and contact me through the details provided there.
"""
    slow_type(stdscr, text)


def main():
    curses.wrapper(cover_letter)


if __name__ == "__main__":
    main()