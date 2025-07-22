
<template>
    <h2>SWIPER DEMO</h2>
    <div class="swiper">
        <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="imgPath in imgPaths"><img :src="imgPath" alt=""></div>
        </div>
        <!-- 如果需要分页器 -->
        <div class="swiper-pagination"></div>
        
        <!-- 如果需要导航按钮 -->
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>
        
    </div>
    导航等组件可以放在Swiper容器之外
</template>



<script>
       
export default {
    mounted(){
        var mySwiper = new Swiper ('.swiper', {
            // direction: 'vertical', // 垂直切换选项
            loop: true, // 循环模式选项
            
            // 如果需要分页器
            pagination: {
            el: '.swiper-pagination',
            },
            
            // 如果需要前进后退按钮
            navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
            },
            
            on: {
                slideChangeTransitionStart: function(){
                console.log("當前輪播 " + this.activeIndex);
                },
            },
        }) 
    },
    data(){
        return {
            imgPaths: ['/src/assets/01.webp','/src/assets/02.webp','/src/assets/03.webp', '/src/assets/04.webp', '/src/assets/05.webp', '/src/assets/06.webp']
        }
    }
}
</script>


<style>
.swiper {
    width: 600px;
    height: 300px;
}
</style>