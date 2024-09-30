

function AppViewModel() {

}

var self = this;

self.project = {
    nowCategory: ko.observable()
}

self.articlesTitle = ko.observableArray([]);
self.articlesFull = ko.observable();

self.articlesTitle(jsonData.posts)
self.articlesTitle(self.articlesTitle().sort((a, b) => a.date < b.date));
self.popular = self.articlesTitle().sort((a, b) => a.likes-a.dislike > b.likes-a.dislike);

self.categoriesTemp = ko.observableArray(["Новое"]);
self.project.nowCategory(self.categoriesTemp()[0]);

jsonData.categories.forEach(element => {
    self.categoriesTemp.push(element.name)
});


// Activates knockout.js
$(document).ready(function() {
    ko.applyBindings(new AppViewModel());
})
