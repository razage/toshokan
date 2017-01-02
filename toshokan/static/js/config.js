'use strict';

require.config({
    baseURL: "js",

    shim: {
        "bootstrap": {
            deps: ['jquery'],
            exports: "Bootstrap"
        },
        "slimscroll": {
            deps: ['jquery'],
            exports: "slimScroll"
        }
    },

    paths: {
        "underscore": "../bower_components/underscore/underscore-min",
        "jquery": "../bower_components/jquery/dist/jquery.min",
        "bootstrap": "../bower_components/bootstrap/dist/js/bootstrap.min",
        "backbone": "../bower_components/backbone/backbone-min",
        "hbs": "../bower_components/require-handlebars-plugin/hbs",
        "validate": "../bower_components/jquery-validation/dist/jquery.validate.min",
        "slimscroll": "../bower_components/jquery-slimscroll/jquery.slimscroll.min"
    }
});

require([
    'jquery',
    'views/topbar',
    'views/sidebar',
    'views/content',
    'bootstrap',
    'slimscroll'
], function($, TopbarView, SidebarView, ContentView) {
    $(".scroll").slimScroll({
        railColor: "#1EBC61",
        color: "#0EAC51",
        railVisible: true,
        height: "auto"
    });
    var topbarView = new TopbarView();
    var sidebarView = new SidebarView();
    var contentView = new ContentView();
});