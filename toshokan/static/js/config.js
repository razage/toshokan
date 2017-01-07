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
        "jquery-ui": "../bower_components/jquery-ui/jquery-ui.min.js",
        "bootstrap": "../bower_components/bootstrap/dist/js/bootstrap.min",
        "backbone": "../bower_components/backbone/backbone-min",
        "hbs": "../bower_components/require-handlebars-plugin/hbs",
        "validate": "../bower_components/jquery-validation/dist/jquery.validate.min",
        "slimscroll": "../bower_components/jquery-slimscroll/jquery.slimscroll.min"
    }
});

require([
    'jquery',
    'backbone',
    'routers/mainRouter',
    'views/topbar',
    'views/sidebar',
    'views/content',
    'bootstrap',
    'slimscroll'
], function($, Backbone, MainRouter, TopbarView, SidebarView, ContentView) {
    var mainRouter = new MainRouter();
    Backbone.history.start();

    var topbarView = new TopbarView();
    var sidebarView = new SidebarView();
    var contentView = new ContentView();
});