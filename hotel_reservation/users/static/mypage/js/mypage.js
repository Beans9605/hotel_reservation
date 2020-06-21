/*img slider*/
const slide_box = document.getElementsByClassName('pic_view_box');
const slides = document.getElementsByClassName('pictures');
const next_btn = document.getElementById('next_btn');
const prev_btn = document.getElementById('prev_btn');
var slide_count = slides.length;
var current_page = 0;

function slide_array() {
    for(var i = 0; i < slide_count; i++){
        slides[i].style.left = i*100 + '%';
    }
}

function move_slide(idx) {
  slide_box[0].style.left = idx * -100 + '%';
  current_page = idx;

}

next_btn.addEventListener('click',function(event){
  event.preventDefault();
  if(current_page < slide_count -1){
    /* 마지막페이지 제외한 페이지가 해당되므로 current_page가 0,1에 해당해야 한다.
    */
  move_slide(current_page + 1);
  } else {
  move_slide(0);
  }
} );

prev_btn.addEventListener('click',function(event){
  event.preventDefault();
  if(current_page > 0){
  move_slide(current_page -1);
  } else {
  move_slide(slide_count -1);
  }
} );


function init(){
    move_slide(0);
    slide_array();
}

init();

/*toggle move*/
const toggle = document.getElementById('toggle');
const toggle_cls_btn = document.getElementById('toggle_cls_btn');
const toggle_open_btn = document.getElementById('toggle_open_btn');
const mypage_text = document.getElementById('mypage_text');




function closeToggle() {
  toggle.classList.add("toggle_close");
  toggle_open_btn.style.visibility = ('visible');
  mypage_text.style.left = 38 + '%';

}

function openToggle() {
  toggle.classList.remove("toggle_close");
  toggle_open_btn.style.visibility = ('hidden');
  mypage_text.style.left = 28 + '%';
}

toggle_cls_btn.addEventListener('click',closeToggle );
toggle_open_btn.addEventListener('click',openToggle );
