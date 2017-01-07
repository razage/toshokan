define([
  'jquery',
  'backbone',
  'bootstrap',
  'slimscroll'
], function($, Backbone) {
    var ContentView = Backbone.View.extend({
        el: ".content",

        events: {
            "click .chapter": "open",
            "click .series": "open",
            "click .volume": "open"
        },

        initialize: function() {
            console.log("Content initialized");
        },

        open: function(e) {
            var $target = $(e.currentTarget),
                urls = {
                    series: "library/" + $target.data("sid"),
                    volume: "library/" + $target.data("sid") + "/" + $target.data("vid"),
                    chapter: "library/" + $target.data("sid") + "/" + $target.data("vid") + "/" + $target.data("cid")
                },
                that = this;

            if ($target.hasClass("series")) {
                Backbone.history.navigate(urls.series, {trigger: true});
            }
            else if ($target.hasClass("volume")) {
                Backbone.history.navigate(urls.volume, {trigger: true});
            }
            else if ($target.hasClass("chapter")) {
                Backbone.history.navigate(urls.chapter, {trigger: true});
            }
        }
    });

    return ContentView;
});