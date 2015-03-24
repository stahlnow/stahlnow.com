/*
  File Uploader app
  */

  var uploader = uploader || {};

  $(function () {

    uploader.File = Backbone.Model.extend({
        url: function () {
            var id = this.id || '';
            return "/api/v1/uploader/file/" + id;
        }
    });

    FileList = Backbone.Collection.extend({
        model: uploader.File,

        // A catcher for the meta object TastyPie will return.
        meta: {},

        // Set the (relative) url to the API for the entry resource.
        url: "/api/v1/uploader/file?sort_by=-created",

        // Our API will return an object with meta, then objects list.
        parse: function (response) {
            this.meta = response.meta;
            return response.objects;
        }
    });

    uploader.Files = new FileList();


    // The visual representation of a single model.
    uploader.FileView = Backbone.View.extend({
        // The element we'll append for the collection models.
        tagName: "li",

        // Cache the template for a single model.
        template: _.template($("#file_template").html()),

        // Bind our events.
        /*
        events: {
            "click .entry": "center"
        },
        */

        // Set up our listeners to model events.
        initialize: function () {
            // (re)Render the view when the model changes
            this.listenTo(this.model, "change", this.render);

            // Remove the view when the model is destroyed
            this.listenTo(this.model, "destroy", this.remove);
        },

        // Render our view to the DOM as a new li (from tagName).
        render: function () {
            var _self = this;

            // Give the list entry an id.
            this.$el.attr("id", this.model.get("id"));

            // Render the template with our model as a JSON object.
            this.$el.html(this.template(this.model.toJSON()));

            return this;
        },


        center: function () {
            //app.map.center(app.map.panTo([this.lat, this.lng]));
        }


    });

    // The view for the entire app.
    uploader.AppView = Backbone.View.extend({
        el: "#uploader",

        events: {
            "change #filePicker": "encode",
            "click #upload": "upload"
        },

        initialize: function () {
            // TastyPie requires us to use a ?format=json param, so we'll set that as a default.
            $.ajaxPrefilter(function (options) {
                _.extend(options, {format: "json"});
            });

            this.listenTo(uploader.Files, "add", this.addFile);

            // cache some elements
            this.$filePicker = this.$("#filePicker");

            this.$fileBase64 = this.$("#fileBase64");

            // fetch all files
            uploader.Files.fetch();
        },

        // Add a single entry
        addFile: function (file) {
            console.log("addFile");
            var view = new uploader.FileView({model: file});
            $("#file_list").append(view.render().el);
        },

        // Clear the list and add each entry one by one.
        addAll: function () {
            this.$("#file_list").html("");
            uploader.Files.each(this.addFile, this);
        },

        // Crate a new todo when the input has focus and enter key is hit.
        encode: function(event) {

            var files = event.target.files;
            var file = files[0];

            if (files && file) {
                var reader = new FileReader();

                reader.onload = function(readerEvt) {
                    var binaryString = readerEvt.target.result;
                    //console.log(this.$filePicker.val())
                    //this.$fileBase64.val(btoa(binaryString));
                    document.getElementById("fileBase64").value = btoa(binaryString);

                };

                reader.readAsBinaryString(file);
            }
        },

        upload: function(event) {
            console.log("upload");
            // Create a new todo.
            uploader.Files.create({name: document.getElementById("filePicker").value, file: document.getElementById("fileBase64").value});
            // Reset the input.
            console.log(document.getElementById("fileBase64").value);
            console.log(document.getElementById("filePicker").value)
            document.getElementById("fileBase64").value = "";
            document.getElementById("filePicker").value = "";
        }
    });

    // And we're off.
    new uploader.AppView();
});



