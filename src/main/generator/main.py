from .lib import Problem, Page, Card, SubmissionDisplay
from .lib.htmllib import *
from .db import listSubKeys, ensureExists, getKey, setKey, deleteKey

def generate(path, contents):
    ensureExists("/code/serve/" + path)
    with open("/code/serve/" + path, "w") as f:
        f.write(str(contents))

def generateLogin():
    generate("login.html", Page(
        div(cls="login-box", contents=[
            h2("Login", cls="login-header"),
            h.label("Username", cls="form-label"),
            h.input(name="username", cls="form-control"),
            h.label("Password", cls="form-label"),
            h.input(name="password", cls="form-control", type="password"),
            div(cls="align-right", contents=[
                h.button("Login", cls="button login-button")
            ])
        ])
    ))

def generateSetup():
    generate("setup.html", Page(
        h2("Setup", cls="page-title"),
        Card("Problems", "Create problems to go in the contests", "/static/problems_mgmt.html"),
        Card("Contests", "Create contests", "/static/contests.html"),
        Card("Users", "Create users who will participate in contests, as well as other admin users who can create and judge contests and problems", "/static/users.html")
    ))

def generateInitialProblems():
    generate("problems.html", Page(
        h1("No problems available yet")
    ))

def generateInitialLeaderboard():
    generate("leaderboard.html", Page(
        h1("Leaderboard not available yet")
    ))

def generateUsersPage():
    generate("users.html", Page(
        h2("Users", cls="page-title"),
        div(cls="actions", contents=[
            h.button("+ Create Admin", cls="button button-blue create-admin"),
            h.button("+ Create Participant", cls="button create-participant")
        ]),
        div(cls="row user-cards")
    ))

def generateContestsPage():
    generate("contests.html", Page(
        h2("Contests", cls="page-title"),
        div(cls="actions", contents=[
            h.button("+ Create Contest", cls="button create-contest")
        ]),
        div(cls="contest-cards")
    ))

class Modal(UIElement):
    def __init__(self, title, body, footer):
        # taken from https://getbootstrap.com/docs/4.1/components/modal/
        self.html = div(cls="modal", role="dialog", contents=[
            div(cls="modal-dialog", role="document", contents=[
                div(cls="modal-content", contents=[
                    div(cls="modal-header", contents=[
                        h.h5(title, cls="modal-title"),
                        h.button(**{"type": "button", "class": "close", "data-dismiss": "modal", "arial-label": "close"}, contents=[
                            h.span("&times;", **{"aria-hidden": "true"})
                        ])
                    ]),
                    div(body, cls="modal-body"),
                    div(footer, cls="modal-footer")
                ])
            ])
        ])

def generateContestPage():
    generate("contest.html", Page(
        h2("Contest", cls="page-title"),
        div(cls="actions", contents=[
            h.button("+ Choose Problem", cls="button choose-problem")
        ]),
        Card("Contest Details", div(cls="contest-details", contents=[
            h.form(cls="row", contents=[
                div(cls="form-group col-12", contents=[
                    h.label(**{"for": "contest-name", "contents":"Name"}),
                    h.input(cls="form-control", name="contest-name", id="contest-name")
                ]),
                div(cls="form-group col-6", contents=[
                    h.label(**{"for": "contest-start-date", "contents":"Start Date"}),
                    h.input(cls="form-control", name="contest-start-date", id="contest-start-date", type="date")
                ]),
                div(cls="form-group col-6", contents=[
                    h.label(**{"for": "contest-start-time", "contents":"Start Time"}),
                    h.input(cls="form-control", name="contest-start-time", id="contest-start-time", type="time")
                ]),
                div(cls="form-group col-6", contents=[
                    h.label(**{"for": "contest-end-date", "contents":"End Date"}),
                    h.input(cls="form-control", name="contest-end-date", id="contest-end-date", type="date")
                ]),
                div(cls="form-group col-6", contents=[
                    h.label(**{"for": "contest-end-time", "contents":"End Time"}),
                    h.input(cls="form-control", name="contest-end-time", id="contest-end-time", type="time")
                ])
            ])
        ])),
        Modal(
            "Choose Problem",
            h.select(cls="form-control problem-choice", contents=[
                h.option("-")
            ]),
            div(
                h.button("Cancel", **{"type":"button", "class": "button button-white", "data-dismiss": "modal"}),
                h.button("Add Problem", **{"type":"button", "class": "button add-problem"})
            )
        ),
        div(cls="problem-cards")
    ))

def generateProblemsMgmtPage():
    generate("problems_mgmt.html", Page(
        h2("Problems", cls="page-title"),
        div(cls="actions", contents=[
            h.button("+ Create Problem", cls="button create-problem")
        ]),
        div(cls="problem-cards")
    ))

def generateProblemMgmtPage():
    generate("problem.html", Page(
        h2("Problem", cls="page-title"),
        Card("Problem Details", div(cls="problem-details", contents=[
            h.form(cls="row", contents=[
                div(cls="form-group col-12", contents=[
                    h.label(**{"for": "problem-title", "contents":"Title"}),
                    h.input(cls="form-control", name="problem-title", id="problem-title")
                ]),
                div(cls="form-group col-12", contents=[
                    h.label(**{"for": "problem-description", "contents":"Description"}),
                    h.textarea(cls="form-control", name="problem-description", id="problem-description")
                ]),
                div(cls="form-group col-12 rich-text", contents=[
                    h.label(**{"for": "problem-statement", "contents":"Problem Statement"}),
                    h.textarea(cls="form-control", name="problem-statement", id="problem-statement")
                ]),
                div(cls="form-group col-12 rich-text", contents=[
                    h.label(**{"for": "problem-input", "contents":"Input Format"}),
                    h.textarea(cls="form-control", name="problem-input", id="problem-input")
                ]),
                div(cls="form-group col-12 rich-text", contents=[
                    h.label(**{"for": "problem-output", "contents":"Output Format"}),
                    h.textarea(cls="form-control", name="problem-output", id="problem-output")
                ]),
                div(cls="form-group col-12 rich-text", contents=[
                    h.label(**{"for": "problem-constraints", "contents":"Constraints"}),
                    h.textarea(cls="form-control", name="problem-constraints", id="problem-constraints")
                ]),
                div(cls="form-group col-12", contents=[
                    h.label(**{"for": "problem-samples", "contents":"Number of Sample Cases"}),
                    h.input(cls="form-control", type="number", name="problem-samples", id="problem-samples")
                ]),
            ])
        ]))
    ))


# Generate static files needed for overall functioning
def generateStatic():
    generateLogin()
    generateSetup()
    # generateInitialProblems()
    generateInitialLeaderboard()
    generateUsersPage()
    generateContestsPage()
    generateContestPage()
    generateProblemsMgmtPage()
    generateProblemMgmtPage()

problemList = []

def generateProblemsPage():
    for problem in problemList:
        generate("problems/{}.html".format(problem.guid), problem.descriptionPage())
    generate("problems.html", Page(
        h.h2("Problems", cls="page-title"),
        *map(lambda x: x.listElem(), problemList)
    ))

def generateProblems():
    global problemList
    problemIds = listSubKeys("/problems")
    curProblems = [Problem(id) for id in problemIds]
    if curProblems != problemList:
        problemList = curProblems
        generateProblemsPage()

def getSubmissionInfo():
    return getKey("/submissionInfo.json") or {}

submissionInfo = getSubmissionInfo()

def generateSubmissionsPage():
    usersToGenerate = {"286030a0-c74a-11e8-9e2c-83267e901a62"}
    for submission in listSubKeys("/newSubmissions"):
        sub = getKey("/submissions/{}/submission.json".format(submission))
        user = sub["user"]
        usersToGenerate.add(user)
        if user not in submissionInfo:
            submissionInfo[user] = []
        submissionInfo[user].append(sub)
        deleteKey("/newSubmissions/" + submission)
    setKey("/submissionInfo.json", submissionInfo)
    for user in usersToGenerate:
        subs = submissionInfo[user]
        subs = sorted(subs, key=lambda sub: int(sub["timestamp"]), reverse=True)
        generate("submissions/{}.html".format(user), Page(
            h2("Your Submissions", cls="page-title"),
            *map(SubmissionDisplay, subs)
        ))

# Generate dynamic files that change occasionally, such as problem statements
# Called once per second
def generateDynamic():
    generateProblems()
    generateSubmissionsPage()
