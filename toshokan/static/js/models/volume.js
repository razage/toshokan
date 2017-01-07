define([
  'backbone'
], function(Backbone, SeriesList) {
    var volume = Backbone.Model.extend({
        urlRoot: "/series",

        url: function() {
            var base = _.result(this, 'urlRoot');
            return base + '/' + encodeURIComponent(this.get('sid')) + '/' + encodeURIComponent(this.id);
        }
    });

    return volume;
});