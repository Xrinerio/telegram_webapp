const main_btn = document.getElementById("1");
const factory_btn = document.getElementById("2");
const friends_btn = document.getElementById("3");
const profile_btn = document.getElementById("4");

let active = main_btn;

main_btn.addEventListener("click", function(e) {
    setmain();
});

factory_btn.addEventListener("click", function(e) {
    setfactory();
});

friends_btn.addEventListener("click", function(e) {
    setfriends();
});

profile_btn.addEventListener("click", function(e) {
    setprofile();
});

function setmain(){
    if(active != main_btn){
        active.classList.remove("active");
        main_btn.classList.add("active");
        active=main_btn;
    }
}

function setfactory(){
    if(active != factory_btn){
        active.classList.remove("active");
        factory_btn.classList.add("active");
        active=factory_btn;
    }
}

function setfriends(){
    if(active != friends_btn){
        active.classList.remove("active");
        friends_btn.classList.add("active");
        active=friends_btn;
    }
}

function setprofile(){
    if(active != profile_btn){
        active.classList.remove("active");
        profile_btn.classList.add("active");
        active=profile_btn;
    }
}

const cookie = document.getElementById("cookie-img");

cookie.addEventListener("click", function(e){
    cookie.style.animation = 'none';
    cookie.offsetHeight;
    cookie.offsetWidth;
    cookie.style.animation = null;
})
