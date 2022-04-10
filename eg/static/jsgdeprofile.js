function chat(){
    console.log("iam in");
    gde=JSON.parse(document.getElementById('gde').textContent);
    url="/chat/"+ gde+"?requestfrom=guide";
    window.location.href=url;
}

function shrevs(){
    document.getElementById("rvs").style.display= 'grid';
}
