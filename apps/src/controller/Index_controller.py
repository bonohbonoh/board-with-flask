from flask import render_template, Blueprint

index_api = Blueprint('index_api', __name__)


@index_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@index_api.route('/board/registration', methods=['GET'])
def registrationBoard():
    return render_template('registrationBoard.html')


@index_api.route('/board/read/<int:boardId>', methods=['GET'])
def readBoard(boardId):
    return render_template('readDetailBoard.html', boardId=boardId)


@index_api.route('/board/update/<int:boardId>', methods=['GET'])
def updateBoard(boardId):
    return render_template('updateBoard.html', boardId=boardId)


@index_api.route('/comment/<int:boardId>', methods=['GET'])
def registrationComment(boardId):
    return render_template('registrationComment.html', boardId=boardId)


@index_api.route('/comment/update/<int:boardId>/<int:commentId>', methods=['GET'])
def updateComment(boardId, commentId):
    return render_template('updateComment.html', boardId=boardId, commentId=commentId)


@index_api.route('/comment/delete/<int:boardId>/<int:commentId>', methods=['GET'])
def deleteComment(boardId, commentId):
    return render_template('deleteComment.html', boardId=boardId, commentId=commentId)


@index_api.route('/signUp', methods=['GET'])
def signupUser():
    return render_template('signUp.html')


@index_api.route('/logIn', methods=['GET'])
def loginUser():
    return render_template('logIn.html')


@index_api.route('/auth', methods=['GET'])
def authUser():
    return render_template('my-page.html')
