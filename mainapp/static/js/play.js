$(document).ready(function () {
    imgSwiper();
});

var myswiper = new Swiper('.swiper-container',{
    direction:'horizontal',
    loop:true,  //循环
    // pagination:'.swiper-pagination',
    paginationClickable:true,  //点击分页器效果
    autoplay:3000,  //自动播放
    //用户触动以后可以继续使用autoplay
    autoplayDisableOnInteraction:false,
    effect: 'cube',
    cube: {
        slideShadows: true,
        shadow: true,
        shadowOffset: 100,
        shadowScale: 0.2
    }
});
