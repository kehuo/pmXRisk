
var path = require('path');
var fs = require('fs');
del = require('del');
var yargs = require('yargs').argv;
var gulp = require('gulp');
var less = require('gulp-less');
var header = require('gulp-header');
var tap = require('gulp-tap');
var nano = require('gulp-cssnano');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var rename = require('gulp-rename');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var rev = require('gulp-rev');
var revCollector = require('gulp-rev-collector');
var browserSync = require('browser-sync');
var pkg = require('./package.json');

var option = {base: 'src'};
var dist = __dirname + '/dist';

gulp.task('build:js', function (){
    gulp.src('src/js/lib/*.js', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
    gulp.src('src/config/**', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
    gulp.src('src/js/*.js', option)
        .pipe(concat('/js/main.js'))
        // .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}))
        //.pipe(uglify())
        .pipe(gulp.dest(dist));
});

gulp.task('build:style', function (){
    var banner = [
        '/*!',
        ' * WeUI v<%= pkg.version %> (<%= pkg.homepage %>)',
        ' * Copyright <%= new Date().getFullYear() %> Tencent, Inc.',
        ' * Licensed under the <%= pkg.license %> license',
        ' */',
        ''].join('\n');
    gulp.src('src/style/weui.less', option)
        .pipe(sourcemaps.init())
        .pipe(less().on('error', function (e) {
            console.error(e.message);
            this.emit('end');
        }))
        .pipe(postcss([autoprefixer(['iOS >= 7', 'Android >= 4.1'])]))
        .pipe(header(banner, { pkg : pkg } ))
        .pipe(sourcemaps.write())
        // .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}))
        .pipe(nano({
            zindex: false,
            autoprefixer: false
        }))
        .pipe(rename(function (path) {
            path.basename += '.min';
        }))
        .pipe(gulp.dest(dist));
    gulp.src('src/style/lib/**', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
    gulp.src('src/style/pmicon/**', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
});

gulp.task('build:favicon', function (){
    gulp.src('src/favicon.ico', option)
        .pipe(gulp.dest(dist));
});

gulp.task('build:data', function (){
    gulp.src('src/data/**', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
});

// //example
// gulp.task('build:example:images', function (){
//     gulp.src('src/example/**/*.?(png|jpg|gif|ico)', option)
//         .pipe(gulp.dest(dist))
//         .pipe(browserSync.reload({stream: true}));
// });
//
// gulp.task('build:example:js', function (){
//     gulp.src('src/example/**/*.js', option)
//         .pipe(concat('/example/example.js'))
//         // .pipe(gulp.dest(dist))
//         .pipe(browserSync.reload({stream: true}))
//         .pipe(uglify())
//         .pipe(gulp.dest(dist));
// });
//
// gulp.task('build:example:style', function (){
//     gulp.src('src/example/example.less', option)
//         .pipe(less().on('error', function (e){
//             console.error(e.message);
//             this.emit('end');
//         }))
//         .pipe(postcss([autoprefixer(['iOS >= 7', 'Android >= 4.1'])]))
//         .pipe(nano({
//             zindex: false,
//             autoprefixer: false
//         }))
//         .pipe(gulp.dest(dist))
//         .pipe(browserSync.reload({stream: true}));
// });
//
// gulp.task('build:example:html', function (){
//     gulp.src('src/example/index.html', option)
//         .pipe(tap(function (file){
//             var dir = path.dirname(file.path);
//             var contents = file.contents.toString();
//             contents = contents.replace(/<link\s+rel="import"\s+href="(.*)">/gi, function (match, $1){
//                 var filename = path.join(dir, $1);
//                 var id = path.basename(filename, '.html');
//                 var content = fs.readFileSync(filename, 'utf-8');
//                 return '<script type="text/html" id="tpl_'+ id +'">\n'+ content +'\n</script>';
//             });
//             file.contents = new Buffer(contents);
//         }))
//         .pipe(gulp.dest(dist))
//         .pipe(browserSync.reload({stream: true}));
// });
//
// gulp.task('build:example', ['build:example:images', 'build:example:js', 'build:example:style', 'build:example:html']);


//pmx start
gulp.task('build:pmx:images', function (){
    var stream = gulp.src('src/pmx/**/*.?(png|jpg|gif|ico|svg)', option)
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
    return stream;
});

gulp.task('build:pmx:js', function (){
    var stream = gulp.src(['src/pmx/**/*.js'], option)
        .pipe(concat('/pmx/pmx.js'))
        .pipe(browserSync.reload({stream: true}))
        //.pipe(uglify())
        //.pipe(gulp.dest(dist));
        .pipe(rev())
        .pipe(gulp.dest(dist))
        .pipe(rev.manifest()) //set hash key json
        .pipe(gulp.dest(dist+'/pmx/rev/js')); //dest hash key json
    return stream;
});

gulp.task('build:pmx:style', function (){
    var stream = gulp.src('src/pmx/pmx.less', option)
        .pipe(less().on('error', function (e){
            console.error(e.message);
            this.emit('end');
        }))
        .pipe(postcss([autoprefixer(['iOS >= 7', 'Android >= 4.1'])]))
        .pipe(nano({
            zindex: false,
            autoprefixer: false
        }))
        // .pipe(gulp.dest(dist))
        .pipe(rev())
        .pipe(gulp.dest(dist))
        .pipe(rev.manifest()) //set hash key json
        .pipe(gulp.dest(dist+'/pmx/rev/css')) //dest hash key json
        .pipe(browserSync.reload({stream: true}));
    return stream;
});

gulp.task('build:pmx:html', function (){
    var stream = gulp.src('src/pmx/index.html', option)
        .pipe(tap(function (file){
            var dir = path.dirname(file.path);
            var contents = file.contents.toString();
            contents = contents.replace(/<link\s+rel="import"\s+href="(.*)">/gi, function (match, $1){
                var filename = path.join(dir, $1);
                var id = path.basename(filename, '.html');
                var content = fs.readFileSync(filename, 'utf-8');
                return '<script type="text/html" id="tpl_'+ id +'">\n'+ content +'\n</script>';
            });
            file.contents = new Buffer(contents);
        }))
        .pipe(gulp.dest(dist))
        .pipe(browserSync.reload({stream: true}));
    return stream;
});

gulp.task('build:pmx', ['build:pmx:images', 'build:pmx:js', 'build:pmx:style', 'build:pmx:html'], function () {
    return gulp.src([dist+'/pmx/rev/**/*.json', dist+'/pmx/index.html'])
        .pipe(revCollector({
            replaceReved: true,
        }))
	    .pipe(gulp.dest(dist+'/pmx'));
    // return gulp.src([dist+'/pmx/**/*.json', dist+'/pmx/index.html'])
    //     .pipe(gulp.dest(dist+'/pmx'));
});
// pmx end∂

gulp.task('debug', ['build:js', 'build:style', 'build:favicon', 'build:pmx']);
gulp.task('release', ['build:js', 'build:style', 'build:favicon', 'build:pmx']);

gulp.task('watch', ['debug'], function () {
    gulp.watch('src/js/*', ['build:js']);
    gulp.watch('src/style/**/*', ['build:style']);

    gulp.watch('src/pmx/pmx.less', ['build:pmx:style']);
    gulp.watch('src/pmx/**/*.?(png|jpg|gif|ico|svg)', ['build:pmx:images']);
    gulp.watch('src/pmx/**/*.js', ['build:pmx:js']);
    gulp.watch('src/**/*.html', ['build:pmx:html']);
});

gulp.task('server', function () {
    yargs.p = yargs.p || 8080;
    browserSync.init({
        server: {
            baseDir: './dist'
        },
        ui: {
            port: yargs.p + 1,
            weinre: {
                port: yargs.p + 2
            }
        },
        port: yargs.p,
        //启动路径
        // startPath: '/example'
        startPath: '/pmx'
    });
});

// 参数说明
//  -w: 实时监听
//  -s: 启动服务器
//  -p: 服务器启动端口，默认8080
gulp.task('default', ['release'], function () {
    if (yargs.s) {
        gulp.start('server');
    }

    if (yargs.w) {
        gulp.start('watch');
    }
});

// Remove all files from dist folder
gulp.task('clean', function(done) {
    del(dist, {
        force: true // clean files outside current directory
    }, done);
});

