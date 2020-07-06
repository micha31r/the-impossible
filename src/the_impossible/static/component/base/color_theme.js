// https://medium.com/@haxzie/dark-and-light-theme-switcher-using-css-variables-and-pure-javascript-zocada-dd0059d72fa2

// function to set a given theme/color-scheme
function set_theme(theme_name) {
    localStorage.setItem('theme', theme_name);
    document.documentElement.className = theme_name;
}

// function to toggle between light and dark theme
function toggle_theme() {
   if (localStorage.getItem('theme') === 'theme-dark'){
       set_theme('theme-light');
   } else {
       set_theme('theme-dark');
   }
}

// Immediately invoked function to set the theme on initial load
auto_run.queue( 
    function () {
        if (localStorage.getItem('theme') === 'theme-dark') {
            set_theme('theme-dark');
        } else {
            set_theme('theme-light');
        }
    }
);