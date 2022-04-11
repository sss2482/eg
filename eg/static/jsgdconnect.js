function chat(){
    c_m=JSON.parse(document.getElementById('c_m').textContent);
    if (c_m=="0"){
        gd=JSON.parse(document.getElementById('gd').textContent);
        url="/chat/"+gd+"?requestfrom=guidee";
        window.location.href=url;
    }
}