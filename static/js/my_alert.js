function my_alert1(content) {
    var M={};
    if(M.dialog){
        return M.dialog.show();
    }
    M.dialog = jqueryAlert({
        'content' : content
    })
}





