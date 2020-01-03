/* global $:true */
+function ($) {
  "use strict";

  var ITEM_ON = "weui-bar-item_on";

  var showTab = function(a) {
    var $a = $(a);
    if($a.hasClass(ITEM_ON)) return;
    var href = $a.attr("href");

    if(!/^#/.test(href)) return ;

    $a.parent().find("."+ITEM_ON).removeClass(ITEM_ON);
    $a.addClass(ITEM_ON);

    var bd = $a.parents(".weui-tab").find(".weui-tab__bd");

    bd.find(".weui-tab__bd-item_active").removeClass("weui-tab__bd-item_active");

    $(href).addClass("weui-tab__bd-item_active");
  }

  $.showTab = showTab;

  $(document).on("click", ".weui-tabbar__item, .weui-navbar_item", function(e) {
    var $a = $(e.currentTarget);
    var href = $a.attr("href");
    if($a.hasClass(ITEM_ON)) return;
    if(!/^#/.test(href)) return;

    e.preventDefault();

    showTab($a);
  });

}($);

