// 주소 값을 받아 주소에 맞는 메뉴 활성화
$('document').ready(function(){
  var path = window.location.pathname.toString().split('/');
  var activePath = path[path.length-1].replace('.html', '');
  
  $('#' + path[path.length-2]).addClass('selected');
  $('#' + path[path.length-2]).find('#' + activePath).addClass('selected');

});

// 스크롤바 적용
const gnbScroll = $('#gnb');
gnbScroll.perfectScrollbar({});

const tableScroll = $('.table-container');
tableScroll.perfectScrollbar({ minScrollbarLength: 20 });

// feather 아이콘 적용
feather.replace();

// gnb 메뉴 slide
$('#gnb .main_menu>li>a').click(function(){
  if($(this).parent().hasClass('selected')){
    return false;
  }
  
  if($(this).parent().hasClass('active')){					
    // $('#gnb .main_menu>li').removeClass('active');
    $(this).parent().removeClass('active');
  }else{
    // $('#gnb .main_menu>li').removeClass('active');
    $(this).parent().addClass('active');
  }
})

// gnb 메뉴 hamburger on/off
var gnbBoolean = true;

$('.feather_gnb').click(function(){
  if(gnbBoolean){
    $('#wrap').addClass('toggle');
  }else {
    $('#wrap').removeClass('toggle');
  }
  
  gnbBoolean = !gnbBoolean;
})

$('.gnb_hover').mouseover(function(){
  if(!gnbBoolean){
    $('#wrap').addClass('over');
    $('#wrap').removeClass('toggle');
  }
})

$('.gnb_hover').mouseleave(function(){
  if(!gnbBoolean){
    $('#wrap').removeClass('over');
    $('#wrap').addClass('toggle');
  }
})

// 실시간 업데이트 애니메이션 작동
function startBtn(){
  $('#progress-bar svg').remove();
  $('.updateBtn').addClass('d-none');
  $('.updateLoading').removeClass('d-none');
  
  var bar = new ProgressBar.Line('#progress-bar', {
      strokeWidth: 2,
      easing: 'easeInOut',
      duration: 1400,
      color: '#008DB1',
      svgStyle: {width: '100%', height: '100%'},
      from: {color: '#008DB1'},
      to: {color: '#016698'},
      step: (state, bar) => {
        bar.path.setAttribute('stroke', state.color);
      },
  });

  bar.animate(1.0,{},function(){
    $('#progress-bar svg').remove();
    $('.updateBtn').removeClass('d-none');
    $('.updateLoading').addClass('d-none');
  });
}


// 필요 함수 정리
/* month, day, hour, minute 형식 변경 */
function dateParse(ti){
  var parse = ti;
  parse = parse < 10 ? `0${parse}` : parse;

  return parse
}

/* json date 형식 변경 */
function jsonDateParse(ti, dataType){
  if(dataType == 'dashboard'){
    var year = ti.substring(0, 4)
    var month = ti.substring(4, 6)
    var day = ti.substring(6, 8)
    var hour = ti.substring(8, 10)
    var minutes = ti.substring(10, 12)
    return `${year}년 ${month}월 ${day}일 ${hour}시 ${minutes}분`;
  }
  
  if(dataType == 'temp'){
    var year = ti.substring(0, 4)
    var month = ti.substring(4, 6)
    var day = ti.substring(6, 8)
    var hour = ti.substring(8, 10)
    var minutes = ti.substring(10, 12)
    return `${year}-${month}-${day} ${hour}:${minutes}`;
  }

  if(dataType == 'hour'){
    var year = ti.substring(0, 4)
    var month = ti.substring(4, 6)
    var day = ti.substring(6, 8)
    var hour = ti.substring(8, 10)
    return `${year}-${month}-${day} ${hour}:00`;
  }

  if(dataType == 'day'){
    var year = ti.substring(0, 4)
    var month = ti.substring(4, 6)
    var day = ti.substring(6, 8)
    return `${year}-${month}-${day}`;
  }
}

/* form 날짜 형식 변경 */
function jsonFormDateParse(ti){
  var parseData = ti.replaceAll(' ','').replaceAll('-','');

  return parseData;
}

/* dygraphs 차트 바 스타일 적용 */
function barChartPlotter(e) {
  var ctx = e.drawingContext;
  var points = e.points;
  var y_bottom = e.dygraph.toDomYCoord(0);

  // Find the minimum separation between x-values.
  // This determines the bar width.
  var min_sep = Infinity;
  for (var i = 1; i < points.length; i++) {
    var sep = points[i].canvasx - points[i - 1].canvasx;
    if (sep < min_sep) min_sep = sep;
  }
  var bar_width = 2.0 / 3 * min_sep;

  // Do the actual plotting.
  for (var i = 0; i < points.length; i++) {
    
    ctx.fillStyle = '#3574F2';

    var p = points[i];
    var center_x = p.canvasx;

    ctx.fillRect(center_x - bar_width / 2, p.canvasy,
        bar_width, y_bottom - p.canvasy);

    /* ctx.strokeRect(center_x - bar_width / 2, p.canvasy,
        bar_width, y_bottom - p.canvasy); */
  }
}

// AHU label Event
$(document).on('change', ".ahu_label_btn", function(){
  const item = $(this);
  if(item.is(':checked')){
    switch (item.data('label')) {
      case "set":
        $('.label_box.set').removeClass('off');
        $('.label.set').removeClass('off');
        $('.tooltipSet').removeClass('d-none');
        $('.circle_y1').removeClass('d-none');
        $('path.line1').removeClass('d-none');
        break;
      case "sup":
        $('.label_box.sup').removeClass('off');
        $('.label.sup').removeClass('off');
        $('.tooltipSup').removeClass('d-none');
        $('.circle_y2').removeClass('d-none');
        $('path.line2').removeClass('d-none');
        break;
      case "ret":
        $('.label_box.ret').removeClass('off');
        $('.label.ret').removeClass('off');
        $('.tooltipRet').removeClass('d-none');
        $('.circle_y3').removeClass('d-none');
        $('path.line3').removeClass('d-none');
        break;
      case "out":
        $('.label_box.out').removeClass('off');
        $('.label.out').removeClass('off');
        $('.tooltipOut').removeClass('d-none');
        $('.circle_y4').removeClass('d-none');
        $('path.line4').removeClass('d-none');
        break;
      default :
        break;
    }
  }else {
    switch (item.data('label')) {
      case "set":
        $('.label_box.set').addClass('off');
        $('.label.set').addClass('off');
        $('.tooltipSet').addClass('d-none');
        $('.circle_y1').addClass('d-none');
        $('path.line1').addClass('d-none');
        break;
      case "sup":
        $('.label_box.sup').addClass('off');
        $('.label.sup').addClass('off');
        $('.tooltipSup').addClass('d-none');
        $('.circle_y2').addClass('d-none');
        $('path.line2').addClass('d-none');
        break;
      case "ret":
        $('.label_box.ret').addClass('off');
        $('.label.ret').addClass('off');
        $('.tooltipRet').addClass('d-none');
        $('.circle_y3').addClass('d-none');
        $('path.line3').addClass('d-none');
        break;
      case "out":
        $('.label_box.out').addClass('off');
        $('.label.out').addClass('off');
        $('.tooltipOut').addClass('d-none');
        $('.circle_y4').addClass('d-none');
        $('path.line4').addClass('d-none');
        break;
      default :
        break;
    }
  }
})