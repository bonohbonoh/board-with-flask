const main = {

    init: function () {
        const _this = this;
        _this.readList();
        $('#btn-update').on('click', function () {
            _this.updateBoard();
        });

        $('#btn-registration').on('click', function () {
            _this.registrationBoard();
        });

        $('#btn-delete').on('click', function () {
            _this.deleteBoard();
        });

        $('#btn-comment-registration').on('click', function () {
            _this.registrationComment();
        });

        $('#btn-comment-update').on('click', function () {
            _this.updateComment();
        });

        $('#btn-sign-up').on('click', function () {
            _this.signUp();
        });

        $('#btn-log-in').on('click', function () {
            _this.logIn();
        });

        $('#btn-log-out').on('click', function () {
            _this.logOut();
        });

        $('#btn-auth').on('click', function () {
            _this.readMyPage();
        });

        _this.readDetail();
    },

    readList: function () {
        $.ajax({
            type: 'GET',
            url: '/api/v1/board/',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: function (response) {
                if (localStorage.getItem("Authorization") == null || localStorage.getItem("Authorization") == "logged-out") {
                    document.getElementById('logged-in-page').style.display = "none";
                    document.getElementById('un-login-page').style.display = "";
                } else {
                    document.getElementById('un-login-page').style.display = "none";
                    document.getElementById('logged-in-page').style.display = "";
                }
                const renderList = document.getElementById('list')
                for (const key in response) {
                    renderList.innerHTML += '<tr><td><a href = /board/read/' + response[key]['id'] + '> ' + response[key]['title'] + '</a></td>' + '<td>' + response[key]['author'] + '</td></tr>'
                }

            }
        })
    },

    readDetail: function () {
        const id = document.getElementById("boardId").value
        const readObj = document.getElementById("readBoardObj")
        $.ajax({
            type: 'GET',
            url: '/api/v1/board/' + id,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: function (response) {
                readObj.title.value = response['title']
                readObj.author.value = response['author']
                readObj.text.value = response['text']
                const comments = response['comments']
                const commentsList = document.getElementById('commentList')

                for (const comment in comments) {
                    commentsList.innerHTML += '<tr><td>' + '<div className="form-group">' +
                        '<input type="text" className="form-control" value = "' + comments[comment]['contents'] + '" readOnly>' +
                        '<br>' +
                        '<a href="/comment/delete/' + id + '/' + comments[comment]['id'] + '" role="button" className="btn btn-danger" style="float: right" >' + '[삭제]' + '</a>' +
                        '<a href="/comment/update/' + id + '/' + comments[comment]['id'] + '" role="button" className="btn btn-primary" style="float: right">' + '[수정]  ' + '</a>' +
                        '</td>' + '<td>' + comments[comment]['author'] +
                        '</td></tr>'
                }
            }
        })
    },

    registrationBoard: function () {
        const data = {
            'title': $('#title').val(),
            'text': $('#text').val(),
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/board/',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function () {
            alert('작성 완료');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    updateBoard: function () {

        const data = {
            title: $('#title').val(),
            text: $('#text').val(),
        };
        const boardId = document.getElementById("boardId").value;
        $.ajax({
            type: 'PATCH',
            url: '/api/v1/board/' + boardId,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function () {
            alert('수정 완료');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });

    },

    deleteBoard: function () {
        const id = $('#boardId').val();
        $.ajax({
            type: 'DELETE',
            url: '/api/v1/board/' + id,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
        }).done(function () {
            alert('삭제 완료');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    updateComment: function () {
        const data = {
            'board_id': $('#boardId').val(),
            'contents': $('#contents').val()
        };
        $.ajax({
            type: 'PATCH',
            url: '/api/v1/comment/' + '/' + commentId,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function () {
            alert('수정 완료');
            window.location.href = '/board/read/' + data.board_id;
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    registrationComment: function () {
        const data = {
            'board_id': $('#boardId').val(),
            'contents': $('#contents').val()
        };
        $.ajax({
            type: 'POST',
            url: '/api/v1/comment/',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function () {
            alert('작성 완료');
            window.location.href = '/board/read/' + data.board_id;
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },


    signUp: function () {
        const data = {
            'email': $('#email').val(),
            'password': $('#password').val(),
            'name': $('#name').val(),
            'nickname': $('#nickname').val(),
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/user',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function () {
            alert('회원가입 완료');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    logIn: function () {
        const data = {
            'email': $('#email').val(),
            'password': $('#password').val(),
        };
        $.ajax({
            type: 'POST',
            url: '/api/v1/user/login',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data),
        }).success(function (response) {
            const token = response['access_token']
            alert('로그인 완료');
            localStorage.setItem("Authorization", token);
            window.location.href = '/';
        }).fail(function (error) {
            alert('잘못된 회원 정보입니다.');
        });
    },

    logOut: function () {
        $.ajax({
            type: 'POST',
            url: '/api/v1/user/logout',
            dataType: 'json',
            contentType: 'application/json',
        }).done(function () {
            alert('로그아웃 완료');
            localStorage.setItem("Authorization", "logged-out")
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    readMyPage: function () {
        const token = localStorage.getItem("Authorization")
        const password = $('#password').val()
        $.ajax({
            type: 'GET',
            url: '/api/v1/user/' + password,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            headers: {"Authorization": token},
        }).done(function (response) {
            document.getElementById("password-banner").style.display = "none"
            document.getElementById("user-info-table").style.display = ""
            const userRenderList = document.getElementById('my-info')
            const boardRenderList = document.getElementById('my-board-list')
            const commentRenderList = document.getElementById('my-comment-list')
            const boards = response['boards']
            const comments = response['comments']
            userRenderList.innerHTML += '<tr><td>' + response['email'] + '</td>' + '<td>' + response['name'] + '</td>' + '<td>' + response['nickname'] + '</td></tr>'

            for (board in boards) {
                boardRenderList.innerHTML += '<tr><td><a href=/board/read/' + boards[board]['id'] + '>' + boards[board]['title'] + '</td></tr>'
            }
            for (comment in comments) {
                commentRenderList.innerHTML += '<tr><td><a href=/board/read/' + comments[comment]['board_id'] + '>' + comments[comment]['contents'] + '</td></tr>'
            }

        }).fail(function () {
            alert('비밀번호가 잘못되었습니다.');
        });
    },


};

main.init();

