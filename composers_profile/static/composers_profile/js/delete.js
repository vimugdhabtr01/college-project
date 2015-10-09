function delete_composer(composer_id){
    $('#modal_delete').modal('show');
    $('#yes').on('click',function(e){
        $(location).attr('href', 'delete/'+composer_id+'/')
    });
}
