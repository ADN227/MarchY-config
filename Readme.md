# Mi configuracion de GNU Linux
![deskys](https://github.com/ADN227/MarchY-config/blob/main/0.jpg)
* **Window manager**
* * xorg
* * Bspwm 
* * Picom
* * Sxhkd
* * Polybar
* **Shell**
* * zsh
* * oh-my-zsh
* **Extras**
* * nitrogen
* * tilix
* * ranger
* * vim
* * xsecurelock
* * neofetch
* * lolcat
* * audacity
* * gimp
* * kdenlive
* * libreoffice
* * xsane
* * discord 
* * brave
* * firefox

## Bspwm 
```
 cp bspwm/bspwmrc ~/.config/bspwm/bspwmrc
```
basado en [wiki de Arch](https://wiki.archlinux.org/title/Bspwm)

## Picom
```
 cp picom/picom.conf ~/.config/picom/picom.conf
```
basado en [wiki de Arch](https://wiki.archlinux.org/title/Picom)

## Sxhkd 
```
 cp sxhkd/sxhkdrc ~/.config/sxhkd/sxhkdrc
```
basado en [wiki de Arch](https://wiki.archlinux.org/title/Sxhkd), [repo de Zatiel](https://github.com/callmezatiel/olddotfiles) y [pastebin](https://pastebin.com/t37b6VQq)

## Polybar
```
 cp polybar/config ~/.config/polybar/config
 cp polybar/dkey.py ~/.config/polybar/dkey.py
 cp polybar/music.py ~/.config/polybar/music.py
```
basado en [wiki de polybar](https://gitlab.com/polybar/polybar/-/wikis/pages)

## zsh y oh my zsh
```
 cp zsh/.zshrc ~/.zshrc
 cp -r zsh/Imagenes ~/Imagenes
 cp zsh/fondo.py ~/fondo.py
 cp zsh/logo ~/logo
```
basado en [github de oh my zsh](https://github.com/ohmyzsh/ohmyzsh)

## neofetch
```
 cp neofetch/config.conf ~/.config/neofetch/config.conf
```
basado en [wiki de neofetch](https://github.com/dylanaraps/neofetch/wiki) y [Repo de lolcat](https://github.com/jaseg/lolcat)

## Grub
```
 cp -r grub2 ~/grub2
```
Editar archivo de grub con **sudo vim /etc/default/grub**: descomentar y cambiar las lineas 
```
GRUB_THEME="/home/usr/grub2/theme.txt"
GRUB_DISABLE_SUBMENU=y
```
Actualizar cambios con
```
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

basado en [wiki de Arch](https://wiki.archlinux.org/title/GRUB) y [Xenlism Grub Theme](https://www.gnome-look.org/p/1440862).

Imagenes extraidas:
[0.jpg](https://images.hdqwalls.com/wallpapers/katana-anime-girl-neon-4k-9s.jpg),
[1.jpg](https://wallpapertag.com/wallpaper/full/3/e/f/199636-dual-monitor-background-3840x1080-for-tablet.jpg),
[2.jpg](https://images6.alphacoders.com/317/317353.jpg),
[3.jpg](http://www.hdwallpaperslife.com/wp-content/uploads/2018/02/katana_anime_girl_4k-HD.jpg),
[4.jpg](https://wallpaperaccess.com/full/2923524.jpg),
[5.jpg](https://uhdpixel.com/wall/fox-forest-trees-mountains-minimalist-minimalism-4k-y7342/),
[6.jpg](https://images.hdqwalls.com/download/1/forest-dark-evening-sunset-last-light-minimalistic-5c-3840x2160.jpg),
[7.jpg](https://images.wallpapersden.com/image/download/desert-towers-cool_bG5sa26UmZqaraWkpJRobWllrWdma2U.jpg),
[8.jpg](https://www.teahub.io/photos/full/52-527219_game-of-thrones-stark-logo-minimalist-8k-macbook.jpg),
[9.jpg](https://wallpaperforu.com/wp-content/uploads/2020/08/minimal-wallpaper-20081414183546-scaled.jpg),
[10.jpg](https://www.pixel4k.com/wp-content/uploads/2018/10/minimalism-logo-devil-4k_1540751406.jpg),
[11.jpg](https://wallpapertops.com/walldb/original/4/f/6/222752.jpg),
[12.jpg](https://wallpaperset.com/w/full/6/6/b/294562.jpg),
[13.jpg](https://images.hdqwalls.com/download/neon-genesis-evangelion-bye-my-friend-4k-bw-2560x1700.jpg),
[14.jpg](https://www.pixel4k.com/wp-content/uploads/2019/11/k-da-pop-stars-neon-akali-league-of-legends-lol-lol_1574104459.jpg),
[15.jpg](https://wallup.net/wp-content/uploads/2015/12/149830-anime-Neon_Genesis_Evangelion.jpg),
[16.jpg](https://images.hdqwalls.com/download/neon-city-pan-4k-20-2560x1440.jpg),
[17.jpg](https://images.hdqwalls.com/download/anime-cyber-girl-neon-city-cr-3840x2160.jpg),
[18.jpg](https://besthqwallpapers.com/img/original/130418/neon-line-circuit-board-neon-digital-background-pink-neon-lines-modern-technology-printed-circuit-board.jpg),
[19.jpg](https://newswatchtv.com/wp-content/uploads/2018/06/iStock-832493292.jpg),
[20.jpg](https://wallpapercave.com/wp/wp5317933.jpg),
[21.jpg](https://www.deviantart.com/spiraloso/art/Phelt-Premium-2K-Wallpaper-897027201),
[22.jpg](https://www.deviantart.com/yiresukam/art/Peyto-Lake-896431115),
[23.jpg](https://www.deviantart.com/djraspberry1999/art/Abstract-Squares-Wallpaper-Minimalist-864513223),
[24.jpg](https://www.deviantart.com/djraspberry1999/art/Abstract-Circles-Wallpaper-Minimalist-866041428),
[25.jpg](https://www.deviantart.com/prisonercoin/art/Calm-Skies-896075094),
[26.jpg](https://www.deviantart.com/bisbiswas/art/Verdant-Mountain-892874939),
[27.jpg](https://www.deviantart.com/hydeillustration/art/Kingdom-of-Fire-892207205)
