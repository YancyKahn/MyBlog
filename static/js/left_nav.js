$(function(){
    var pathname = window.location.pathname;
    console.log(pathname);
    if(pathname.indexOf("user/profile/") >= 0 ) {
        $("#id_profile").addClass("active");
    }
    if(pathname.indexOf("user/subscribe/") >= 0 ) {
        $("#id_subscribe").addClass("active");
    }
    if(pathname.indexOf("user/change_password/") >= 0 ) {
        $("#id_password").addClass("active");
    }
    if(pathname.indexOf("user/feedback/") >= 0 ) {
        $("#id_feedback").addClass("active");
    }
});
