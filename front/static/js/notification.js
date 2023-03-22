if("Notification" in window){	
	Notification.requestPermission();
}

Notification.requestPermission(function (result){
	// 권한 거절        
	if(result == 'denied' && localStorage.getItem('notification') != 'false') {
		alert('알림을 차단하셨습니다.\n브라우저의 사이트 설정에서 변경하실 수 있습니다.');
		localStorage.setItem('notification','false');
		return false;
	}else if(result == 'granted') {
		localStorage.setItem('notification','true');
	}
});

/* 페이지 내 업데이트 알림 구현 중 false -> true */
var windowBlur = false;

$(window).blur(function(){
	windowBlur = true;
});
$(window).focus(function(){
	windowBlur = false;
});