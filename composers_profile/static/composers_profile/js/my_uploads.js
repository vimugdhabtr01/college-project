$(function(){
    $.get(
        "https://www.googleapis.com/youtube/v3/search"{
            part: 'snippet',
            maxResults = 10,
            key = '660478359243-4u455gipq1lotnohau35apcph0sk4nmf.apps.googleusercontent.com'},
            function(data){
                $.each(data.items, function(i, item){
                alert(item);
                })
            }
        )
});
