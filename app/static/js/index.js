function FileHelper()

{
    FileHelper.readStringFromFileAtPath = function(pathOfFileToReadFrom)
    {
        var request = new XMLHttpRequest();
        request.open("GET", pathOfFileToReadFrom, false);
        request.send(null);
        var returnValue = request.responseText;

        return returnValue;
    }
}


const main_btn = document.getElementById("1");
const factory_btn = document.getElementById("2");
const friends_btn = document.getElementById("3");
const profile_btn = document.getElementById("4");

const main_page = document.getElementsByClassName("wrapper")[0];
const cookie_ico = document.getElementsByClassName("currency")[0];
const container = document.getElementsByClassName("container")[0];

let active = main_btn;

const pageURL = new URL("static/txt/", location.origin)
const factory_page = new DOMParser().parseFromString(FileHelper.pathOfFileToReadFrom(pageURL+"factory.txt"), "text/html").getElementsByClassName("wrapper")[0];
const imgURL = new URL("static/png/", location.origin);
console.log(imgURL)
let list_el = `<div class="list-el"><div class="list-el-ico"><img src="${imgURL+"farm.png"}" alt=""></div><div class="list-el-text"><h3 id="el-name">Cookies Farm</h3><hr><div class="line"><p id="income-count">123</p><p>cookie/hour</p></div><div class="line"><p id="income-count">2</p><p>you have</p></div><div class="line"><p id="income-count">246</p><p>all income</p></div></div><div class="el-btn">2000$</div></div>`
let factory_list_el = new DOMParser().parseFromString(list_el, "text/html").getElementsByClassName("list-el")[0];


main_btn.addEventListener("click", function(e) {
    try{
        document.getElementsByClassName("wrapper")[0].remove();
    }catch{}
    setmain();
});

factory_btn.addEventListener("click", function(e) {
    try{
        document.getElementsByClassName("wrapper")[0].remove();
    }catch{}
    
    setfactory();
});

friends_btn.addEventListener("click", function(e) {
    try{
        document.getElementsByClassName("wrapper")[0].remove();
    }catch{}
    setfriends();
});

profile_btn.addEventListener("click", function(e) {
    try{
        document.getElementsByClassName("wrapper")[0].remove();
    }catch{}
    setprofile();
});

function setmain(){
    if(active != main_btn){
        active.classList.remove("active");
        active.querySelector(".ico").classList.remove("active-svg");
        main_btn.classList.add("active");
        main_btn.querySelector(".ico").classList.add("active-svg");
        active=main_btn;
        
        container.appendChild(main_page);
    }
}

function setfactory(){
    if(active != factory_btn){
        active.classList.remove("active");
        active.querySelector(".ico").classList.remove("active-svg");
        factory_btn.classList.add("active");
        factory_btn.querySelector(".ico").classList.add("active-svg");
        active=factory_btn;
    }
}

function setfriends(){
    if(active != friends_btn){
        active.classList.remove("active");
        active.querySelector(".ico").classList.remove("active-svg");
        friends_btn.classList.add("active");
        friends_btn.querySelector(".ico").classList.add("active-svg");
        active=friends_btn;
        
        container.appendChild(factory_page);
    }
}

function setprofile(){
    if(active != profile_btn){
        active.classList.remove("active");
        active.querySelector(".ico").classList.remove("active-svg");
        profile_btn.classList.add("active");
        profile_btn.querySelector(".ico").classList.add("active-svg");
        active=profile_btn;
    }
}

const cookie = document.getElementById("cookie-img");

if(active == main_page){
    cookie.addEventListener("click", function(e){
        cookie.style.animation = 'none';
        cookie.offsetHeight;
        cookie.offsetWidth;
        cookie.style.animation = null;
    })
};


const ttst = document.getElementById("ttst");
const list = document.getElementsByClassName("list-box")[0];
ttst.addEventListener("click", function(e){
    ttst.style.background = "red";
    var i = factory_list_el;
    list.append(i);
})