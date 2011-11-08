var feedback = {};
feedback.init = function(config) {
    if (!(config.button && config.drop && config.popup))
        throw "invalid params";
    config.popup.find('form.feedback').ajaxSubmit({
        'onstart':function(){
            config.popup.addClass('loading');
        },
        'onend':function(){
            config.popup.removeClass('loading');
        },
        'onerror':function(why){
            alert('Error! '+why);
        },
        'onsuccess':feedback.done(config)
    });

    config.button.click(function(){
        config.drop.removeClass('hiding');
        config.popup.removeClass('hiding');
        config.popup.find('input[name=email]').focus();
    });
    config.popup.find('.close').click(feedback.closeit(config));
};

feedback.done = function(config) {
    return function() {
        config.popup.addClass('thanks');
        config.popup.delay(1000).fadeOut(500, feedback.closeit(config));
        config.popup.delay(1000).fadeOut(500);
    };
};

feedback.closeit = function(config) {
    return function(){
        config.drop.addClass('hiding');
        config.popup.addClass('hiding');
        config.popup.removeClass('thanks');
        config.popup.css('display','');
        config.drop.css('display','');
        config.popup.find('textarea').val('');
        config.popup.find('input[name=subject]').val('');
    };
};

var callback = {};
callback.init = function(config) {
    if (!(config.button && config.drop && config.popup))
        throw "invalid params";
    config.popup.find('form.callback').ajaxSubmit({
        'onstart':function(){
            config.popup.addClass('loading');
        },
        'onend':function(){
            config.popup.removeClass('loading');
        },
        'onerror':function(why){
            alert('Error! '+why);
        },
        'onsuccess':callback.done(config)
    });

    config.button.click(function(){
        config.drop.removeClass('hiding');
        config.popup.removeClass('hiding');
//        config.popup.find('input[name=username]').focus();
    });
    config.popup.find('.close').click(callback.closeit(config));
};

callback.done = function(config) {
    return function() {
        config.popup.addClass('thanks');
        config.popup.delay(1000).fadeOut(500, callback.closeit(config));
        config.popup.delay(1000).fadeOut(500);
    };
};

callback.closeit = function(config) {
    return function(){
        config.drop.addClass('hiding');
        config.popup.addClass('hiding');
        config.popup.removeClass('thanks');
        config.popup.css('display','');
        config.drop.css('display','');
//        config.popup.find('input[name=subject]').val('');
    };
};

//check_shipping_method = function() {
//    if ($("[value='pickup_process']").prop("selected")) {
//        $("#id_ship-address").closest("tr").hide();
//    } else {
//        $("#id_ship-address").closest("tr").show();
//    }
//};

$(document).ready(function(){
    $('a [href^="skype"]').click(function(){return skypeCheck()});
    $("a[rel^='prettyPhoto']").prettyPhoto({theme: 'light_rounded'});

//    check_shipping_method();
    feedback.init({
        'button':$('#feedback_button'),
        'drop':$('#feedback_drop'),
        'popup':$('#feedback_popup')
    });

    callback.init({
        'button':$('.callback_button'),
        'drop':$('#callback_drop'),
        'popup':$('#callback_popup')
    });

//    $("#id_shipping_method").change(check_shipping_method);
    $(".rate i").mouseover(function(){
        $(this).add($(this).nextAll("i")).addClass("active");
        $(this).prevAll("i").addClass("inactive");
        $(".hint").show();
    });
    $(".rate i").mouseleave(function(){
        $(".rate i").removeClass("active");
        $(".rate i").removeClass("inactive");
        $(".hint").hide();
    });

    $(".rate i").click(function() {
        var params = $(this).attr("id").match(/(\d+)/g);
        $.get(
            '/rating/vote/',
            {'product': params[0], 'score': params[1]},
            function(data) {
                $("#hint-for-"+params[0]).text('голос учтен!');
            },
            'json'
        );
    });
    $(".brief .image").click(function(){
        document.location = $(this).closest(".brief").find("a").first().attr("href");
    });
    $(".brief.cigarette .add-info").click(function(){
        document.location = $(this).closest(".brief").find("a").first().attr("href");
    });
    $(".leftside .ammo").click(function(){
        document.location = $(this).prev("h2").find("a").first().attr("href");
    });
    $(".manufacturer-list img").click(function(){
        document.location = $(this).parent("div").next("h2").find("a").first().attr("href");
    });
    $(".manufacturer-list .desc .moreinfo").click(function(){
        document.location = $(this).closest("li").children("h2").find("a").first().attr("href");
    });
    $(".header .logo").click(function(){
        document.location = '/';
    });
});

reformal_wdg_w    = "713";
reformal_wdg_h    = "460";
reformal_wdg_domain    = "e-cigar";
reformal_wdg_mode    = 0;
reformal_wdg_title   = "Электронные сигареты";
reformal_wdg_ltitle  = "Оставьте свой отзыв";
reformal_wdg_lfont   = "";
reformal_wdg_lsize   = "";
reformal_wdg_color   = "#549c45";
reformal_wdg_bcolor  = "#516683";
reformal_wdg_tcolor  = "#FFFFFF";
reformal_wdg_align   = "right";
reformal_wdg_charset = "utf-8";
reformal_wdg_waction = 0;
reformal_wdg_vcolor  = "#9FCE54";
reformal_wdg_cmline  = "#E0E0E0";
reformal_wdg_glcolor  = "#105895";
reformal_wdg_tbcolor  = "#FFFFFF";
reformal_wdg_tcolor_aw4  = "#3F4543";
reformal_wdg_bimage = "7688f5685f7701e97daa5497d3d9c745.png";
