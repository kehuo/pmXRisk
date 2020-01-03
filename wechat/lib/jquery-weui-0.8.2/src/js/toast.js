+ function($) {
  "use strict";

  var defaults;
  
  var show = function(html, otherStyle) {
    var mask = $("<div class='weui-mask-transparent'></div>").appendTo(document.body);

    var tpl = '<div class="weui-toast" style="'+ otherStyle +'">' + html + '</div>';
    var dialog = $(tpl).appendTo(document.body);

    dialog.addClass("weui-toast-visible");
  };

  var hide = function(callback) {
    $(".weui-mask-transparent").remove();
    $(".weui-toast-visible").removeClass("weui-toast-visible").transitionEnd(function() {
      var $this = $(this);
      $this.remove();
      callback && callback($this);
    });
  }

  $.toast = function(text, style, callback) {
    if(typeof style === "function") {
      callback = style;
    }
    var className = "weui-icon-success-no-circle";
    var otherStyle = "";
    if(style == "cancel") {
      className = "weui-icon-cancel";
    } else if(style == "forbidden") {
      className = "weui-icon-warn";
    } else if(style == "text") {
      className = "";
      otherStyle = "min-height:0;";
    }
    show('<i class="weui-icon_toast '+ className +'"></i><p class="weui-toast__content">' + (text || "已经完成") + '</p>', otherStyle);

    setTimeout(function() {
      hide(callback);
    }, toastDefaults.duration);
  }

  $.showLoading = function(text) {
    show('<i class="weui-loading weui-icon_toast"></i><p class="weui-toast__content">' + (text || "数据加载中") + '</p>', '');
  }

  $.hideLoading = function() {
    hide();
  }

  var toastDefaults = $.toast.prototype.defaults = {
    duration: 2000
  }

}($);
