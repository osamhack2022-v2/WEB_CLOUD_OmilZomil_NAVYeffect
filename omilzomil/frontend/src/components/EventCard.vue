<template>
  <div
    class="overlay"
    @click.self="$emit('closeCard')"
  >
    <div class="card">
      <div class="background">
        <img 
          class="star1" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star2" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star3" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star4" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star5" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star6" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star7" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star8" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star9" 
          src="@/assets/images/fire/light.svg" 
        >
        <img 
          class="star10" 
          src="@/assets/images/fire/light.svg" 
        >
      </div>
      <button
        class="x"
        @click="$emit('closeCard')"
      />
      <div class="textbox">
        <div class="text1">
          {{ name }}
        </div>
        <div class="text2">
          {{ contents }}
        </div>
      </div>
      <div
        v-if="photo===null"
        class="image"
      >
        <img
          class="back"
          src="@/assets/images/fire/back.svg" 
        >
        <img
          class="one"
          src="@/assets/images/fire/one.svg" 
        >
        <img
          class="two"
          src="@/assets/images/fire/two.svg" 
        >
        <img
          class="three"
          src="@/assets/images/fire/three.svg" 
        >
        <img
          class="four"
          src="@/assets/images/fire/four.svg" 
        >
        <img
          class="five"
          src="@/assets/images/fire/red.svg" 
        >
        <img
          class="six"
          src="@/assets/images/fire/yellow.svg" 
        >
        <img
          class="seven"
          src="@/assets/images/fire/red.svg" 
        >
        <img
          class="eight"
          src="@/assets/images/fire/yellow.svg" 
        >
        <img
          class="nine"
          src="@/assets/images/fire/blue.svg" 
        >
      </div>
      <div
        v-else
        class="photoclap"
      >
        <img
          class="photoback"
        >
        <img
          class="photo"
          :src="photo"
          @error="e => e.target.src = require('@/assets/images/test.png')"
        >
        <img
          class="backhand"
          src="@/assets/images/clap/back.svg"
        >
        <img
          class="fronthand"
          src="@/assets/images/clap/front.svg"
        >
        <img
          class="clapeffect"
          src="@/assets/images/clap/effect.svg"
        > 
      </div>
    </div> 
  </div>
</template>

<script>
export default {
    props:{
        name:{
            type:String,
            default:null
        },
        contents:{
            type:String,
            default:null
        },
        photo:{
          type:String,
          default:null
        }
    },
    emits: ["closeCard"],
}
</script>

<style scoped>

.overlay{
  position: fixed;
  /* display:none; */
  display:flex;
  justify-content: center;
  align-items: center;
  width:100%;
  height:100%;
  top:0;
  left:0;
  right:0;
  bottom:0;
  background-color:rgba(0,0,0,0.5);
  z-index:1000000;
}
    @keyframes blink{
      0% {opacity:0;}
      100% {opacity:1;}
    }
    @keyframes effect{
      0%{transform: scale(1);}
      100%{transform: scale(1.3);}
    }
    @keyframes boom {
        0% {
            transform: scale(0.8);
            transform-origin: 0% 100%;
        }
        50% {
            transform: scale(1);
            transform-origin: 0% 100%;
        }
        /* 100% {
            transform: scale(0.9);
            transform-origin: 0% 100%;    
        } */
    }
    @keyframes scale-up-br {
        0% {
            transform: scale(0.2);
            transform-origin: 100% 100%;
        }
        100% {
            transform: scale(1);
            transform-origin: 100% 100%;
        }
    }
    @keyframes scale-up-bl {
        0% {
            transform: scale(0.2);
            transform-origin: 0% 100%;
        }
        100% {
            transform: scale(1);
            transform-origin: 0% 100%;
        }
    }
    @keyframes slide-tr {
        0% {
            transform-origin: 0% 100%;
            transform: scale(0.2) translateY(80px) translateX(-60%);
        }
        100% {
            transform-origin: 100% 100%;
            transform: scale(1) translateY(0) translateX(0);
        }
    }
    @keyframes slide-right {
        0% {
            transform-origin: 0% 0%;
            transform: scaleX(0.3) translateY(40px) translateX(-80px);
        }
        100% {
            transform-origin: 0% 0%;
            transform: scaleX(1.0) translateY(0) translateX(0px);
        }
    }
    @keyframes ball {
        0% {
            left: 34.62%;
            right: 57.87%;
            top: 52.99%;
            bottom: 39.49%;
        }
    }
    @keyframes shake1 {
      from {
        transform: scale(0.9) rotate(-5deg);
        /* transform: translateY(100px); */
        /* opacity: 0; */
      }
      to {
        transform: scale(1) rotate(0);
        /* transform: translateY(0); */
        /* opacity: 1; */
      }
    }
    @keyframes shake2 {
      from {
        transform: scale(1.1) rotate(5deg);
        /* transform: translateY(100px); */
        /* opacity: 0; */
      }
      to {
        transform: scale(1) rotate(0);
        /* transform: translateY(0); */
        /* opacity: 1; */
      }
    }
    .card{
        position:relative;
        display: flex;
        width: 400px;
        height: 600px;
        gap:50px;
        flex-direction: column;

        background: linear-gradient(180deg, #47237D 0%, #623FAC 49.83%, #47237D 100%);
    }
    .background{
        position:absolute;
        width: 400px;
        height: 600px;
    }
    .background .star1{
      position:absolute;
      width:10px;
      top:40px;
      left:30px;
      animation:blink 2s ease-in-out infinite alternate;
    }
    .background .star1{
      position:absolute;
      width:10px;
      top:40px;
      left:30px;
      animation:blink 2s ease-in-out infinite alternate;
    }
    .background .star2{
      position:absolute;
      width:9px;
      top:91px;
      left:120px;
      animation:blink 1.3s ease-in-out infinite alternate;
    }
    .background .star3{
      position:absolute;
      width:14px;
      top:34px;
      left:201px;
      animation:blink 1.1s ease-in-out infinite alternate;
    }
    .background .star4{
      position:absolute;
      width:20px;
      top:201px;
      left:40px;
      animation:blink 2s ease-in-out infinite alternate;
    }
    .background .star5{
      position:absolute;
      width:17px;
      top:180px;
      left:276px;
      animation:blink 2.6s ease-in-out infinite alternate;
    }
    .background .star6{
      position:absolute;
      width:21px;
      top:377px;
      left:248px;
      animation:blink 1.7s ease-in-out infinite alternate;
    }
    .background .star7{
      position:absolute;
      width:9px;
      top:409px;
      left:30px;
      animation:blink 1s ease-in-out infinite alternate;
    }
    .background .star8{
      position:absolute;
      width:15px;
      top:30px;
      left:329px;
      animation:blink 2s ease-in-out infinite alternate;
    }
    .background .star9{
      position:absolute;
      width:14px;
      top:503px;
      left:319px;
      animation:blink 0.9s ease-in-out infinite alternate;
    }
    .background .star10{
      position:absolute;
      width:21px;
      top:531px;
      left:229px;
      animation:blink 2s ease-in-out infinite alternate;
    }
    .card .textbox{
        display:flex;
        width:100%;
        gap:5px;
        z-index: 1;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding:0px 10px;
        box-sizing:border-box;
    }
    .card .textbox .text1{
        font-style: normal;
        font-weight: 700;
        font-size: 24px;
        line-height: 28px;
        text-align: center;
        word-break: normal;
        color: #F9F9FB;
        width:100%;
    }
    .card .textbox .text2{
        font-style: normal;
        font-weight: 500;
        font-size: 20px;
        line-height: 23px;
        text-align: center;
        letter-spacing: -0.055em;
        color: #F9F9FB;
        white-space:nowrap
        /* word-break:normal; */
    }
    .card .image{
        position:relative;
        width:234px;
        height:234px;
    }
    .card .image .back{
        position: absolute;
        left: 8.04%;
        right: 38.33%;
        top: 38.05%;
        bottom: 6.37%;
        animation: boom 2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
    }
    .card .image .one{
        position: absolute;
        z-index: 1;
        left: 23.08%;
        right: 61.34%;
        top: 6.41%;
        bottom: 49.74%;
        animation: scale-up-br 1s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
    }
    .card .image .two{
        position: absolute;
        z-index: 2;
        left: 43.16%;
        right: 1.1%;
        top: 44.87%;
        bottom: 28.61%;
        animation: scale-up-bl 1s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
    }
    .card .image .three{
        position: absolute;
        left: 39.61%;
        right: 37.47%;
        top: 6.5%;
        bottom: 58.82%;
        animation: slide-tr 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .four{
        position: absolute;
        left: 61.5%;
        right: 8.89%;
        top: 33.87%;
        bottom: 52.7%;
        animation: slide-right 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .five{
        position: absolute;
        left: 11.64%;
        right: 80.84%;
        top: 21.58%;
        bottom: 70.9%;
        animation: ball 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .six{
        position: absolute;
        left: 40.17%;
        right: 52.31%;
        top: 6.41%;
        bottom: 86.07%;
        animation: ball 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .seven{
        position: absolute;
        left: 70.69%;
        right: 21.79%;
        top: 18.16%;
        bottom: 74.32%;
        animation: ball 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .eight{
        position: absolute;
        left: 73.84%;
        right: 18.64%;
        top: 67.82%;
        bottom: 24.66%;
        animation: ball 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .image .nine{
        position: absolute;
        left: 42.98%;
        right: 49.5%;
        top: 46.24%;
        bottom: 46.24%;
        animation: ball 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    .card .x{
        background: url("@/assets/images/x.svg") no-repeat;
        position: absolute;
        border:none;
        cursor:pointer;
        top:14px;
        right:15px;
        width: 24px;
        height: 24px;
    }
    .card .photoclap{
      position:relative;
      width: 400px;
      height: 236px;
    }
    .card .photoclap .photoback{
      position: absolute;
      width: 236px;
      height: 236px;
      top:0;
      left:82px;
      filter: blur(16px);
      border-radius: 165px;
      background: rgba(255, 255, 255, 0.5);
      animation:blink 1s ease-in-out infinite alternate;
    }
    .card  .photoclap .photo{
      position: absolute;
      width: 236px;
      height: 236px;
      top:0;
      left:82px;
      border-radius: 165px;
    }
    .card .fronthand{
      position:absolute;
      z-index: 3;
      height: 93.42px;
      width: 80.06px;
      left:240.03px;
      top: 170.34px;
      animation: shake2 0.2s infinite alternate;
    }
    .card .backhand{
      position:absolute;
      height:92.23px;
      width:67.07px;
      left:218.03px;
      top:171.66px;
      z-index: 2;
      animation: shake1 0.2s infinite alternate;
    }
    .card .clapeffect{
      position:absolute;
      width:27.79px;
      height:30.03px;
      left:208.36px;
      top:152.28px;
      z-index: 2;
      animation: effect 0.2s infinite alternate;
    }
</style>