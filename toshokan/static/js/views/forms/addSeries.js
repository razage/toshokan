define([
  'jquery',
  'backbone',
  'hbs!templates/addSeries',
  'bootstrap'
], function($, Backbone, AddSeriesTemplate) {
    var AddSeriesView = Backbone.View.extend({
        el: ".viewbox",

        events: {},

        initialize: function() {
            console.log("AddSeriesView initialized");
        },

        render: function() {
            var addSeriesTemplate = AddSeriesTemplate({});
            this.$el.html(addSeriesTemplate);
        }
    });

    return AddSeriesView;
});