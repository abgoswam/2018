$( document ).ready(function() {
  // window.alert('The document is ready!!!! JQuery is working');

  // $('button').click(function() {
  //   window.alert('Hello Friend. How are you');
  // })

  $('#add-class').click(function(){
    $('button').addClass('super-button');
  })

  $('#remove-class').click(function(){
    $('button').removeClass('super-button');
  })

  $('#toggle-class').click(function(){
    $('button').toggleClass('super-button');
  })

  $('.click-this').click(function(){
    $(this).toggleClass('click-this');
  })

  $('#delete-list').click(function(){
    $('#item-list').children().first().remove();
  })

  $('ul').click(function(){
    // $(this).parent().text('we just changed something');
    $(this).siblings().text('we just changed something');
  })

});
