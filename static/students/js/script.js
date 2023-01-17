function hideSidebar() {
   var sidebar = document.getElementById('sidebar')
    var right_col = document.getElementById('right-col')


    if (sidebar.style.display === 'block') {
       sidebar.style.display = 'none'
        right_col.style.width = "100" + '%'

    } else if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block'
        right_col.style.width = "80" + '%'

    }

}