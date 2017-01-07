define([
  'backbone'
], function(Backbone, SeriesList) {
    var series = Backbone.Model.extend({
        urlRoot: "/series"
    });

    return series;
});