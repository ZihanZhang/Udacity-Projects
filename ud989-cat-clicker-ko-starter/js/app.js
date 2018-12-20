var Cat = function() {
    this.clickCount = ko.observable(0);
    this.name = ko.observable('Tabby');
    this.imgSrc = ko.observable('img/22252709_010df3379e_z.jpg');
    this.age = ko.observable('Infant');
    this.nicknames = ko.observableArray([{nickname: 'Zihan'}, {nickname: 'Dudu'}, {nickname: 'Dudu pig'}]);
}

var ViewModel = function() {
    this.currentCat = ko.observable( new Cat());

    this.incrementCounter = function() {
        this.clickCount(this.clickCount() + 1);
        if (this.clickCount() > 30) {
            this.age('Teen');
        }
        if (this.clickCount() > 50) {
            this.age('Mature');
        }
        if (this.clickCount() > 60) {
            this.age('Elderly');
        }
    };
}

ko.applyBindings(new ViewModel());