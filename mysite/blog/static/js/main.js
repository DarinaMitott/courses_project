
$('#search_again').click(function (e) {
    e.preventDefault();
    $('input[name="query"]').focus();
})

$('.cat-fact-btn').click(function (e) {
    e.preventDefault();
    $.getJSON('https://catfact.ninja/fact?max_length=50').done(function (data) {
        $('#cat-fact-alert').text(data.fact);
        $('#cat-fact-alert').fadeTo(2000, 700).slideUp(500, function(){
            $("#cat-fact-alert").slideUp(500);
        });
    })
})