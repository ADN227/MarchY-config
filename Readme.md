# Mi configuracion de GNU Linux
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

##zsh y oh my zsh
```
 cp zsh/.zshrc ~/.zshrc
 cp -r zsh/Imagenes ~/Imagenes
 cp zsh/fondo.py ~/fondo.py
 cp zsh/logo ~/logo
```
basado en [github de oh my zsh](https://github.com/ohmyzsh/ohmyzsh)

##neofetch
```
 cp neofetch/config.conf ~/.config/neofetch/config.conf
```
basado en [wiki de neofetch](https://github.com/dylanaraps/neofetch/wiki) y [Repo de lolcat](https://github.com/jaseg/lolcat)

##Grub
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

basado en [wiki de Arch](https://wiki.archlinux.org/title/GRUB) y [Xenlism Grub Theme](https://www.gnome-look.org/p/1440862)
