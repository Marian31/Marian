function addUser(){
    const user = {
        first_name : $('#first_name').val(),
        mid_name : $('#mid_name').val(),
        last_name : $('#last_name').val(),
    };
    $.ajax({
        url: 'user/add',
        type: 'POST',
        contentType: 'application/json',
        data: user,
        success: function (result) {
            location.reload();
        }
    });
}
function deleteUser(id){
   $.ajax({
        url: '/' + id,
        type: 'DELETE',
        success: function (result) {
            location.reload();
        }
    });
}
function addAlbum(){
    const album = {
        album_title: $('#album_title').val(),
        genre: $('#genre').val(),
        protected: $('#protected').val()
    };
    $.ajax({
        url: '/album/add',
        type: 'POST',
        contentType: 'application/json',
        data: album,
        success: function (result) {
            location.reload();
        }
    });
}

function deleteAlbum(id){
    $.ajax({
        url: '/2/' + id,
        type: 'DELETE',
        success: function (result) {
            location.reload();
        }
    });
}

function addSong(){
    const song = {
        artist : $('#artist').val(),
        song_title: $('#song_title').val(),
    };
    $.ajax({
        url: '/song/add',
        type: 'POST',
        contentType: 'application/json',
        data: song,
        success: function (result) {
            location.reload();
        }
    });
}

function deleteSong(id){
    $.ajax({
        url: '/song/' + id,
        type: 'DELETE',
        success: function (result) {
            location.reload();
        }
    });
}
