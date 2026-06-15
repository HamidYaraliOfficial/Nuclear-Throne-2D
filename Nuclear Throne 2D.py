import sys, math, random, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ───────────────────────────────────────────────────────────────────────────────
# TRANSLATIONS
# ───────────────────────────────────────────────────────────────────────────────
TR = {
    "en": {
        "title": "Nuclear Throne 2D", "score": "Score", "best": "Best",
        "wave": "Wave", "kills": "Kills", "hp": "HP", "ammo": "Ammo",
        "start": "▶  Start Game", "restart": "↺  Restart", "pause": "⏸  Pause",
        "resume": "▶  Resume", "theme": "Theme", "language": "Language",
        "light": "Light", "dark": "Dark", "game_over": "GAME OVER",
        "new_best": "🏆 NEW BEST!", "paused": "PAUSED", "attempts": "Runs",
        "weapon": "Weapon", "controls": "WASD Move  |  Mouse Aim & Shoot  |  R Reload  |  1-3 Weapon",
        "level": "Level", "xp": "XP", "fps": "FPS",
    },
    "zh": {
        "title": "核王座2D", "score": "分数", "best": "最佳",
        "wave": "波次", "kills": "击杀", "hp": "生命", "ammo": "弹药",
        "start": "▶  开始游戏", "restart": "↺  重新开始", "pause": "⏸  暂停",
        "resume": "▶  继续", "theme": "主题", "language": "语言",
        "light": "浅色", "dark": "深色", "game_over": "游戏结束",
        "new_best": "🏆 新纪录!", "paused": "已暂停", "attempts": "次数",
        "weapon": "武器", "controls": "WASD移动 | 鼠标瞄准射击 | R换弹 | 1-3切换武器",
        "level": "等级", "xp": "经验", "fps": "帧率",
    },
    "fa": {
        "title": "تخت هسته‌ای 2D", "score": "امتیاز", "best": "بهترین",
        "wave": "موج", "kills": "کشته", "hp": "جان", "ammo": "گلوله",
        "start": "▶  شروع بازی", "restart": "↺  شروع مجدد", "pause": "⏸  مکث",
        "resume": "▶  ادامه", "theme": "تم", "language": "زبان",
        "light": "روشن", "dark": "تاریک", "game_over": "بازی تمام شد",
        "new_best": "🏆 رکورد جدید!", "paused": "مکث", "attempts": "دفعات",
        "weapon": "سلاح", "controls": "WASD حرکت | ماوس نشانه | R شارژ | 1-3 سلاح",
        "level": "سطح", "xp": "تجربه", "fps": "FPS",
    },
}

# ───────────────────────────────────────────────────────────────────────────────
# THEMES
# ───────────────────────────────────────────────────────────────────────────────
THEMES = {
    "dark": {
        "name": "dark",
        "win_bg": "#0A0A14", "panel_bg": "#0D0D1E", "panel_border": "#1A1A35",
        "text": "#E0E8FF", "text2": "#5560A0", "accent": "#FF4500",
        "btn_bg": "#16213E", "btn_h": "#0F3460", "btn_txt": "#E0E8FF",
        "btn2_bg": "#1A3320", "btn2_h": "#245030",
        "btn3_bg": "#3A1010", "btn3_h": "#5A1818",
        "cmb_bg": "#0D0D1E", "cmb_border": "#1A1A35",
        "floor": "#1A1A28", "floor2": "#141420", "floor_line": "#252540",
        "wall": "#0A0A18", "wall_border": "#1E1E3A",
        "player_body": "#00CCFF", "player_glow": "#0088FF",
        "player_leg": "#0066CC", "player_head": "#00FFFF",
        "bullet_player": "#FFFF00", "bullet_player2": "#FF8800",
        "bullet_enemy": "#FF2200", "bullet_enemy2": "#FF6600",
        "enemy1": "#FF2244", "enemy1_2": "#AA0022",
        "enemy2": "#FF8800", "enemy2_2": "#CC5500",
        "enemy3": "#AA00FF", "enemy3_2": "#6600CC",
        "enemy_boss": "#FF0066", "enemy_boss2": "#880033",
        "hud_bg": "#0D0D1E99", "hud_text": "#E0E8FF",
        "hp_bar": "#FF2244", "hp_bar2": "#880011",
        "ammo_bar": "#FFCC00", "xp_bar": "#00CCFF",
        "particle_hit": "#FF6600", "particle_death": "#FF2244",
        "pickup_hp": "#FF2244", "pickup_ammo": "#FFCC00",
        "pickup_xp": "#00CCFF", "pickup_weapon": "#FF00FF",
        "overlay_bg": "#000D",
        "shadow": "#00000080",
        "muzzle": "#FFFFA0",
        "crosshair": "#FF4500",
    },
    "light": {
        "name": "light",
        "win_bg": "#D0D8F0", "panel_bg": "#E8EEF8", "panel_border": "#B0BCD8",
        "text": "#1A1A3E", "text2": "#505080", "accent": "#CC2200",
        "btn_bg": "#4A70C9", "btn_h": "#2050A8", "btn_txt": "#FFFFFF",
        "btn2_bg": "#2A7040", "btn2_h": "#1A5030",
        "btn3_bg": "#C03020", "btn3_h": "#A01808",
        "cmb_bg": "#E0E8F8", "cmb_border": "#A0B0D0",
        "floor": "#C8D4E8", "floor2": "#B8C8DC", "floor_line": "#A8B8CC",
        "wall": "#8090B0", "wall_border": "#6070A0",
        "player_body": "#0066AA", "player_glow": "#0088CC",
        "player_leg": "#004488", "player_head": "#00AADD",
        "bullet_player": "#CC8800", "bullet_player2": "#AA5500",
        "bullet_enemy": "#CC0000", "bullet_enemy2": "#880000",
        "enemy1": "#CC1133", "enemy1_2": "#880022",
        "enemy2": "#CC6600", "enemy2_2": "#884400",
        "enemy3": "#8800CC", "enemy3_2": "#550088",
        "enemy_boss": "#CC0055", "enemy_boss2": "#880033",
        "hud_bg": "#E8EEF8CC", "hud_text": "#1A1A3E",
        "hp_bar": "#DD1133", "hp_bar2": "#880011",
        "ammo_bar": "#CC9900", "xp_bar": "#0088AA",
        "particle_hit": "#FF6600", "particle_death": "#CC1133",
        "pickup_hp": "#CC1133", "pickup_ammo": "#CC9900",
        "pickup_xp": "#0088AA", "pickup_weapon": "#9900CC",
        "overlay_bg": "#0008",
        "shadow": "#00000040",
        "muzzle": "#FFEE88",
        "crosshair": "#CC2200",
    },
}

# ───────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ───────────────────────────────────────────────────────────────────────────────
BASE_W, BASE_H = 880, 580
TILE = 40
MAP_COLS, MAP_ROWS = 26, 18
PLAYER_SPEED = 3.2
BULLET_SPEED = 11.0
FPS = 60

WEAPONS = [
    {"name": "Pistol",    "dmg": 18, "spd": 12, "spread": 0.05, "burst": 1,
     "reload": 30,  "mag": 12, "auto": False, "color": "#FFFF00"},
    {"name": "Shotgun",   "dmg": 22, "spd": 9,  "spread": 0.35, "burst": 5,
     "reload": 55,  "mag": 6,  "auto": False, "color": "#FF8800"},
    {"name": "Minigun",   "dmg": 10, "spd": 14, "spread": 0.12, "burst": 1,
     "reload": 8,   "mag": 60, "auto": True,  "color": "#00FFFF"},
]


# ───────────────────────────────────────────────────────────────────────────────
# PARTICLE
# ───────────────────────────────────────────────────────────────────────────────
class Particle:
    __slots__ = ("x","y","vx","vy","color","size","life","max_life","shape","gravity")

    def __init__(self, x, y, color, vx=None, vy=None, size=None, life=None,
                 shape="circle", gravity=0.15):
        self.x = float(x); self.y = float(y)
        self.color = color
        self.vx = vx if vx is not None else random.uniform(-4, 4)
        self.vy = vy if vy is not None else random.uniform(-5, 1)
        self.size = size if size is not None else random.uniform(2, 7)
        self.life = life if life is not None else random.randint(15, 35)
        self.max_life = self.life
        self.shape = shape
        self.gravity = gravity

    def update(self):
        self.x += self.vx; self.y += self.vy
        self.vy += self.gravity
        self.vx *= 0.92
        self.life -= 1

    def draw(self, p: QPainter):
        ratio = self.life / self.max_life
        a = int(255 * ratio)
        c = QColor(self.color); c.setAlpha(max(0, a))
        p.setBrush(QBrush(c)); p.setPen(Qt.PenStyle.NoPen)
        s = self.size * ratio
        if self.shape == "rect":
            p.drawRect(QRectF(self.x - s/2, self.y - s/2, s, s))
        else:
            p.drawEllipse(QRectF(self.x - s/2, self.y - s/2, s, s))


# ───────────────────────────────────────────────────────────────────────────────
# BULLET
# ───────────────────────────────────────────────────────────────────────────────
class Bullet:
    __slots__ = ("x","y","vx","vy","dmg","is_player","alive","color","trail","r")

    def __init__(self, x, y, angle, speed, dmg, is_player, color):
        self.x = float(x); self.y = float(y)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.dmg = dmg
        self.is_player = is_player
        self.alive = True
        self.color = color
        self.trail: list[tuple[float,float]] = []
        self.r = 4

    def update(self):
        self.trail.append((self.x, self.y))
        if len(self.trail) > 6:
            self.trail.pop(0)
        self.x += self.vx; self.y += self.vy

    def draw(self, p: QPainter, t: dict):
        # Trail
        for i, (tx, ty) in enumerate(self.trail):
            a = int(180 * i / len(self.trail))
            c = QColor(self.color); c.setAlpha(a)
            p.setBrush(QBrush(c)); p.setPen(Qt.PenStyle.NoPen)
            s = self.r * i / len(self.trail)
            p.drawEllipse(QRectF(tx - s/2, ty - s/2, s, s))
        # Glow
        gc = QColor(self.color); gc.setAlpha(60)
        p.setBrush(QBrush(gc)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x - self.r*2, self.y - self.r*2,
                             self.r*4, self.r*4))
        # Core
        grad = QRadialGradient(self.x, self.y, self.r)
        grad.setColorAt(0, QColor("#FFFFFF"))
        grad.setColorAt(0.5, QColor(self.color))
        grad.setColorAt(1, QColor(self.color).darker(150))
        p.setBrush(QBrush(grad)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x - self.r, self.y - self.r,
                             self.r*2, self.r*2))


# ───────────────────────────────────────────────────────────────────────────────
# PICKUP
# ───────────────────────────────────────────────────────────────────────────────
class Pickup:
    def __init__(self, x, y, kind):
        self.x = float(x); self.y = float(y)
        self.kind = kind  # "hp","ammo","xp","weapon"
        self.r = 10
        self.anim = random.uniform(0, 360)
        self.alive = True
        self.value = {"hp": 25, "ammo": 20, "xp": 30, "weapon": 0}[kind]

    def update(self):
        self.anim = (self.anim + 3) % 360

    def draw(self, p: QPainter, t: dict):
        colors = {"hp": t["pickup_hp"], "ammo": t["pickup_ammo"],
                  "xp": t["pickup_xp"], "weapon": t["pickup_weapon"]}
        icons  = {"hp": "♥", "ammo": "•", "xp": "★", "weapon": "⚡"}
        c = QColor(colors[self.kind])
        pulse = abs(math.sin(math.radians(self.anim))) * 3
        r = self.r + pulse
        # Glow
        gc = QColor(c); gc.setAlpha(60)
        p.setBrush(QBrush(gc)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x-r-5, self.y-r-5, (r+5)*2, (r+5)*2))
        # Body
        grad = QRadialGradient(self.x, self.y, r)
        grad.setColorAt(0, QColor("#FFFFFF"))
        grad.setColorAt(0.4, c)
        grad.setColorAt(1, c.darker(150))
        p.setBrush(QBrush(grad))
        p.setPen(QPen(c.darker(130), 1.5))
        p.drawEllipse(QRectF(self.x-r, self.y-r, r*2, r*2))
        # Icon
        p.setPen(QPen(QColor("#FFFFFF")))
        p.setFont(QFont("Arial", int(r*0.85), QFont.Weight.Bold))
        p.drawText(QRectF(self.x-r, self.y-r, r*2, r*2),
                   Qt.AlignmentFlag.AlignCenter, icons[self.kind])


# ───────────────────────────────────────────────────────────────────────────────
# ENEMY
# ───────────────────────────────────────────────────────────────────────────────
class Enemy:
    def __init__(self, x, y, kind, wave):
        self.x = float(x); self.y = float(y)
        self.kind = kind  # 1,2,3,"boss"
        scale = 1.0 + wave * 0.08
        stats = {
            1: {"hp": int(40*scale),  "spd": 1.6, "r": 14, "dmg": 12, "shoot": False, "score": 10},
            2: {"hp": int(70*scale),  "spd": 1.1, "r": 18, "dmg": 20, "shoot": True,  "score": 20},
            3: {"hp": int(30*scale),  "spd": 2.4, "r": 11, "dmg": 8,  "shoot": False, "score": 15},
            "boss": {"hp": int(500*scale), "spd": 0.7, "r": 30, "dmg": 35, "shoot": True, "score": 150},
        }
        s = stats[kind]
        self.hp = s["hp"]; self.max_hp = s["hp"]
        self.spd = s["spd"]; self.r = s["r"]
        self.contact_dmg = s["dmg"]; self.shoots = s["shoot"]
        self.score_val = s["score"]
        self.alive = True
        self.shoot_timer = random.randint(60, 120)
        self.anim = random.uniform(0, 360)
        self.vx = 0.0; self.vy = 0.0
        self.hit_flash = 0
        self.facing = 0.0

    def update(self, px, py, walls: list, bullets_out: list, t: dict, wave: int):
        self.anim = (self.anim + 4) % 360
        if self.hit_flash > 0:
            self.hit_flash -= 1

        dx = px - self.x; dy = py - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.facing = math.atan2(dy, dx)
            ndx = dx/dist; ndy = dy/dist
            self.vx = ndx * self.spd
            self.vy = ndy * self.spd

        # Wall avoidance
        nx = self.x + self.vx; ny = self.y + self.vy
        col_x = False; col_y = False
        for (wx, wy, ww, wh) in walls:
            if (nx - self.r < wx+ww and nx + self.r > wx and
                    self.y - self.r < wy+wh and self.y + self.r > wy):
                col_x = True
            if (self.x - self.r < wx+ww and self.x + self.r > wx and
                    ny - self.r < wy+wh and ny + self.r > wy):
                col_y = True
        if not col_x: self.x += self.vx
        if not col_y: self.y += self.vy

        # Shoot
        if self.shoots:
            self.shoot_timer -= 1
            if self.shoot_timer <= 0:
                self.shoot_timer = random.randint(80, 160)
                if dist < 420:
                    spd = 6.0
                    c_e = t["bullet_enemy"]
                    bullets_out.append(Bullet(self.x, self.y, self.facing,
                                              spd, self.contact_dmg // 2,
                                              False, c_e))

    def take_hit(self, dmg):
        self.hp -= dmg
        self.hit_flash = 8
        if self.hp <= 0:
            self.alive = False

    def draw(self, p: QPainter, t: dict):
        colors = {1: (t["enemy1"], t["enemy1_2"]),
                  2: (t["enemy2"], t["enemy2_2"]),
                  3: (t["enemy3"], t["enemy3_2"]),
                  "boss": (t["enemy_boss"], t["enemy_boss2"])}
        c1, c2 = colors[self.kind]

        pulse = abs(math.sin(math.radians(self.anim))) * 2
        r = self.r + pulse

        # Shadow
        sc = QColor(t["shadow"])
        p.setBrush(QBrush(sc)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x - r*0.8, self.y + r*0.6, r*1.6, r*0.5))

        # Glow if hit
        if self.hit_flash > 0:
            gc = QColor("#FFFFFF"); gc.setAlpha(180)
            p.setBrush(QBrush(gc)); p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QRectF(self.x-r-4, self.y-r-4, (r+4)*2, (r+4)*2))

        # Body
        grad = QRadialGradient(self.x - r*0.3, self.y - r*0.3, r*1.4)
        grad.setColorAt(0, QColor(c1).lighter(160))
        grad.setColorAt(0.5, QColor(c1))
        grad.setColorAt(1, QColor(c2))
        p.setBrush(QBrush(grad))
        p.setPen(QPen(QColor(c2).darker(130), 2))

        if self.kind == "boss":
            # Spiky boss shape
            path = QPainterPath()
            spikes = 8
            for i in range(spikes * 2):
                angle = math.radians(i * 180 / spikes + self.anim * 0.5)
                rr = r if i % 2 == 0 else r * 0.6
                xi = self.x + math.cos(angle) * rr
                yi = self.y + math.sin(angle) * rr
                if i == 0: path.moveTo(xi, yi)
                else: path.lineTo(xi, yi)
            path.closeSubpath()
            p.drawPath(path)
        elif self.kind == 3:
            # Fast runner - elongated
            p.save()
            p.translate(self.x, self.y)
            p.rotate(math.degrees(self.facing))
            p.drawEllipse(QRectF(-r*1.4, -r*0.7, r*2.8, r*1.4))
            p.restore()
        else:
            p.drawEllipse(QRectF(self.x-r, self.y-r, r*2, r*2))

        # Eyes
        eye_angle = self.facing
        ex = self.x + math.cos(eye_angle) * r * 0.5
        ey = self.y + math.sin(eye_angle) * r * 0.5
        eye_r = max(3, r * 0.25)
        p.setBrush(QBrush(QColor("#FF0000"))); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(ex - eye_r + math.cos(eye_angle+0.6)*eye_r,
                             ey - eye_r + math.sin(eye_angle+0.6)*eye_r,
                             eye_r*2, eye_r*2))
        p.drawEllipse(QRectF(ex - eye_r + math.cos(eye_angle-0.6)*eye_r,
                             ey - eye_r + math.sin(eye_angle-0.6)*eye_r,
                             eye_r*2, eye_r*2))

        # HP bar
        bar_w = r * 2.5
        bar_x = self.x - bar_w / 2
        bar_y = self.y - r - 10
        p.setBrush(QBrush(QColor(t["hp_bar2"]))); p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(QRectF(bar_x, bar_y, bar_w, 5), 2, 2)
        hp_ratio = max(0, self.hp / self.max_hp)
        p.setBrush(QBrush(QColor(t["hp_bar"])))
        p.drawRoundedRect(QRectF(bar_x, bar_y, bar_w * hp_ratio, 5), 2, 2)


# ───────────────────────────────────────────────────────────────────────────────
# PLAYER
# ───────────────────────────────────────────────────────────────────────────────
class Player:
    def __init__(self, x, y):
        self.x = float(x); self.y = float(y)
        self.r = 16
        self.hp = 100; self.max_hp = 100
        self.vx = 0.0; self.vy = 0.0
        self.facing = 0.0
        self.alive = True
        self.invincible = 0
        self.anim_tick = 0
        self.weapon_idx = 0
        self.weapons = [dict(w) for w in WEAPONS]
        for w in self.weapons:
            w["cur_ammo"] = w["mag"]
            w["reload_timer"] = 0
        self.shoot_timer = 0
        self.muzzle_flash = 0
        self.score = 0
        self.kills = 0
        self.level = 1
        self.xp = 0
        self.xp_next = 100
        self.trail: list[dict] = []
        self.dash_timer = 0

    @property
    def weapon(self):
        return self.weapons[self.weapon_idx]

    def update(self, keys_held: set, walls: list):
        self.anim_tick += 1
        if self.invincible > 0:
            self.invincible -= 1

        dx = dy = 0
        if Qt.Key.Key_W in keys_held or Qt.Key.Key_Up in keys_held: dy -= 1
        if Qt.Key.Key_S in keys_held or Qt.Key.Key_Down in keys_held: dy += 1
        if Qt.Key.Key_A in keys_held or Qt.Key.Key_Left in keys_held: dx -= 1
        if Qt.Key.Key_D in keys_held or Qt.Key.Key_Right in keys_held: dx += 1

        if dx != 0 and dy != 0:
            dx *= 0.707; dy *= 0.707

        self.vx = dx * PLAYER_SPEED
        self.vy = dy * PLAYER_SPEED

        # Wall collision
        nx = self.x + self.vx; ny = self.y + self.vy
        col_x = col_y = False
        for (wx, wy, ww, wh) in walls:
            if (nx-self.r < wx+ww and nx+self.r > wx and
                    self.y-self.r < wy+wh and self.y+self.r > wy):
                col_x = True
            if (self.x-self.r < wx+ww and self.x+self.r > wx and
                    ny-self.r < wy+wh and ny+self.r > wy):
                col_y = True
        if not col_x: self.x += self.vx
        if not col_y: self.y += self.vy

        # Reload
        w = self.weapon
        if w["reload_timer"] > 0:
            w["reload_timer"] -= 1
            if w["reload_timer"] == 0:
                w["cur_ammo"] = w["mag"]

        if self.shoot_timer > 0:
            self.shoot_timer -= 1
        if self.muzzle_flash > 0:
            self.muzzle_flash -= 1

        # Trail
        if dx != 0 or dy != 0:
            self.trail.append({"x": self.x, "y": self.y, "a": 120})
        if len(self.trail) > 8:
            self.trail.pop(0)
        for tr in self.trail:
            tr["a"] = max(0, tr["a"] - 18)

        # XP Level up
        if self.xp >= self.xp_next:
            self.xp -= self.xp_next
            self.level += 1
            self.xp_next = int(self.xp_next * 1.4)
            self.max_hp = min(200, self.max_hp + 15)
            self.hp = min(self.hp + 30, self.max_hp)

    def try_shoot(self, mx, my, bullets_out: list, particles_out: list, t: dict):
        w = self.weapon
        if w["reload_timer"] > 0 or self.shoot_timer > 0:
            return False
        if w["cur_ammo"] <= 0:
            self.reload()
            return False
        angle = math.atan2(my - self.y, mx - self.x)
        for _ in range(w["burst"]):
            sp = w["spread"]
            a = angle + random.uniform(-sp, sp)
            bsp = w["spd"] + random.uniform(-0.5, 0.5)
            bullets_out.append(Bullet(self.x + math.cos(angle)*self.r*1.2,
                                       self.y + math.sin(angle)*self.r*1.2,
                                       a, bsp, w["dmg"], True, w["color"]))
        w["cur_ammo"] -= 1
        self.shoot_timer = w["reload"]
        self.muzzle_flash = 5
        # Muzzle particles
        for _ in range(4):
            particles_out.append(Particle(
                self.x + math.cos(angle)*self.r*1.5,
                self.y + math.sin(angle)*self.r*1.5,
                t["muzzle"], vx=math.cos(angle)*random.uniform(2,6)+random.uniform(-2,2),
                vy=math.sin(angle)*random.uniform(2,6)+random.uniform(-2,2),
                size=random.uniform(2,5), life=8, gravity=0.05))
        return True

    def reload(self):
        w = self.weapon
        if w["reload_timer"] == 0 and w["cur_ammo"] < w["mag"]:
            w["reload_timer"] = w["reload"] * 3

    def take_hit(self, dmg):
        if self.invincible > 0:
            return
        self.hp -= dmg
        self.invincible = 45
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def draw(self, p: QPainter, t: dict):
        # Trail
        for i, tr in enumerate(self.trail):
            a = int(tr["a"] * (i+1) / len(self.trail))
            if a <= 0: continue
            c = QColor(t["player_glow"]); c.setAlpha(a)
            p.setBrush(QBrush(c)); p.setPen(Qt.PenStyle.NoPen)
            s = self.r * (i+1) / len(self.trail) * 0.8
            p.drawEllipse(QRectF(tr["x"]-s, tr["y"]-s, s*2, s*2))

        if not self.alive:
            return
        if self.invincible > 0 and (self.invincible // 4) % 2 == 1:
            return

        # Shadow
        sc = QColor(t["shadow"])
        p.setBrush(QBrush(sc)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x-self.r*0.9, self.y+self.r*0.5,
                             self.r*1.8, self.r*0.5))

        # Outer glow
        pulse = abs(math.sin(self.anim_tick * 0.06)) * 6
        gc = QColor(t["player_glow"]); gc.setAlpha(60)
        p.setBrush(QBrush(gc)); p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QRectF(self.x-self.r-pulse, self.y-self.r-pulse,
                             (self.r+pulse)*2, (self.r+pulse)*2))

        # Body
        grad = QRadialGradient(self.x-self.r*0.3, self.y-self.r*0.3, self.r*1.5)
        grad.setColorAt(0, QColor(t["player_head"]))
        grad.setColorAt(0.5, QColor(t["player_body"]))
        grad.setColorAt(1, QColor(t["player_leg"]))
        p.setBrush(QBrush(grad))
        p.setPen(QPen(QColor(t["player_leg"]).darker(130), 2))
        p.drawEllipse(QRectF(self.x-self.r, self.y-self.r, self.r*2, self.r*2))

        # Direction indicator (gun barrel)
        bx = self.x + math.cos(self.facing)*self.r*0.9
        by = self.y + math.sin(self.facing)*self.r*0.9
        ex = self.x + math.cos(self.facing)*self.r*1.8
        ey = self.y + math.sin(self.facing)*self.r*1.8

        if self.muzzle_flash > 0:
            # Muzzle flash
            mc = QColor(t["muzzle"]); mc.setAlpha(200)
            p.setBrush(QBrush(mc)); p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QRectF(ex-7, ey-7, 14, 14))

        p.setPen(QPen(QColor(self.weapon["color"]), 4,
                      Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        p.drawLine(QPointF(bx, by), QPointF(ex, ey))

        # Eyes (two white dots)
        perp = self.facing + math.pi / 2
        for sign in (-1, 1):
            ex2 = self.x + math.cos(self.facing)*self.r*0.4 + math.cos(perp)*sign*5
            ey2 = self.y + math.sin(self.facing)*self.r*0.4 + math.sin(perp)*sign*5
            p.setBrush(QBrush(QColor("#FFFFFF"))); p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QRectF(ex2-3, ey2-3, 6, 6))
            p.setBrush(QBrush(QColor("#000033")))
            p.drawEllipse(QRectF(ex2-1.5, ey2-1.5, 3, 3))


# ───────────────────────────────────────────────────────────────────────────────
# GAME WIDGET
# ───────────────────────────────────────────────────────────────────────────────
class GameWidget(QWidget):
    sig_score    = pyqtSignal(int)
    sig_best     = pyqtSignal(int)
    sig_wave     = pyqtSignal(int)
    sig_kills    = pyqtSignal(int)
    sig_hp       = pyqtSignal(int, int)
    sig_ammo     = pyqtSignal(int, int)
    sig_level    = pyqtSignal(int)
    sig_xp       = pyqtSignal(int, int)
    sig_weapon   = pyqtSignal(str)
    sig_dead     = pyqtSignal(int, int)
    sig_attempts = pyqtSignal(int)
    sig_fps      = pyqtSignal(int)

    def __init__(self, theme: dict, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.setMinimumSize(400, 260)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.state = "idle"
        self.best = 0
        self.attempts = 0
        self.keys_held: set = set()
        self.mouse_x = 0.0; self.mouse_y = 0.0
        self.mouse_down = False

        self.player: Player = None
        self.enemies: list[Enemy] = []
        self.bullets: list[Bullet] = []
        self.particles: list[Particle] = []
        self.pickups: list[Pickup] = []
        self.walls: list[tuple] = []
        self.floor_tiles: list[tuple] = []

        self.wave = 0
        self.wave_timer = 0
        self.spawn_queue = []
        self.spawn_timer = 0
        self.enemies_this_wave = 0
        self.enemies_killed_wave = 0

        self._last_time = time.perf_counter()
        self._fps_counter = 0
        self._fps_val = 0
        self._fps_timer = 0

        self.camera_x = 0.0; self.camera_y = 0.0

        self.map_w = MAP_COLS * TILE
        self.map_h = MAP_ROWS * TILE

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._loop)
        self.timer.setInterval(1000 // FPS)

    def resizeEvent(self, e):
        super().resizeEvent(e)

    def set_theme(self, theme):
        self.theme = theme
        self.update()

    def _build_map(self):
        self.walls.clear()
        self.floor_tiles.clear()
        # Floor tiles
        for row in range(MAP_ROWS):
            for col in range(MAP_COLS):
                self.floor_tiles.append((col*TILE, row*TILE, TILE, TILE))

        # Border walls
        thick = TILE
        self.walls.append((0, 0, self.map_w, thick))                        # top
        self.walls.append((0, self.map_h-thick, self.map_w, thick))         # bottom
        self.walls.append((0, 0, thick, self.map_h))                        # left
        self.walls.append((self.map_w-thick, 0, thick, self.map_h))         # right

        # Random interior walls
        random.seed(self.wave * 17 + 42)
        for _ in range(12 + self.wave):
            col = random.randint(2, MAP_COLS - 4)
            row = random.randint(2, MAP_ROWS - 4)
            length = random.randint(2, 5)
            horiz = random.random() > 0.5
            for k in range(length):
                if horiz:
                    wx = (col + k) * TILE; wy = row * TILE
                else:
                    wx = col * TILE; wy = (row + k) * TILE
                # Don't block center spawn area
                if (abs(wx - self.map_w//2) > TILE*3 or
                        abs(wy - self.map_h//2) > TILE*3):
                    self.walls.append((wx, wy, TILE, TILE))

    def _start_wave(self):
        self.wave += 1
        self._build_map()
        types = [1, 2, 3]
        base_count = 5 + self.wave * 3
        self.enemies_this_wave = base_count
        self.enemies_killed_wave = 0
        self.spawn_queue = []
        for _ in range(base_count):
            kind = random.choices(types, [0.4, 0.3, 0.3])[0]
            self.spawn_queue.append(kind)
        if self.wave % 5 == 0:
            self.spawn_queue.append("boss")
            self.enemies_this_wave += 1
        self.spawn_timer = 0
        self.sig_wave.emit(self.wave)

    def start(self):
        self.attempts += 1
        self.sig_attempts.emit(self.attempts)
        self.wave = 0
        self.particles.clear(); self.bullets.clear()
        self.enemies.clear(); self.pickups.clear()
        self.spawn_queue.clear()
        cx = MAP_COLS * TILE / 2; cy = MAP_ROWS * TILE / 2
        self.player = Player(cx, cy)
        self.camera_x = cx - self.width()/2
        self.camera_y = cy - self.height()/2
        self.state = "playing"
        self._start_wave()
        self.timer.start()
        self.setFocus()

    def pause_toggle(self):
        if self.state == "playing":
            self.state = "paused"; self.timer.stop()
        elif self.state == "paused":
            self.state = "playing"; self.timer.start(); self.setFocus()
        self.update()

    def _loop(self):
        if self.state != "playing":
            return

        now = time.perf_counter()
        self._fps_counter += 1
        self._fps_timer += 1
        if self._fps_timer >= FPS:
            self._fps_val = self._fps_counter
            self._fps_counter = 0
            self._fps_timer = 0
            self.sig_fps.emit(self._fps_val)
        self._last_time = now

        pl = self.player
        t = self.theme

        # Player update
        pl.update(self.keys_held, self.walls)

        # Mouse to world coords
        wx = self.mouse_x + self.camera_x
        wy = self.mouse_y + self.camera_y
        pl.facing = math.atan2(wy - pl.y, wx - pl.x)

        # Auto shoot
        w = pl.weapon
        if self.mouse_down and (w["auto"] or w["reload"] <= 30):
            pl.try_shoot(wx, wy, self.bullets, self.particles, t)
        elif self.mouse_down and not w["auto"]:
            pass  # handled in mousePressEvent for non-auto

        # Spawn enemies
        if self.spawn_queue:
            self.spawn_timer -= 1
            if self.spawn_timer <= 0:
                self.spawn_timer = max(20, 60 - self.wave * 3)
                kind = self.spawn_queue.pop(0)
                # Spawn at map edge away from player
                for _ in range(50):
                    ex = random.uniform(TILE*1.5, self.map_w - TILE*1.5)
                    ey = random.uniform(TILE*1.5, self.map_h - TILE*1.5)
                    if math.hypot(ex-pl.x, ey-pl.y) > 180:
                        r_e = 30 if kind == "boss" else 18
                        ok = True
                        for (wxx, wyy, www, whh) in self.walls:
                            if (ex-r_e < wxx+www and ex+r_e > wxx and
                                    ey-r_e < wyy+whh and ey+r_e > wyy):
                                ok = False; break
                        if ok:
                            self.enemies.append(Enemy(ex, ey, kind, self.wave))
                            break

        # Update enemies
        new_bullets: list[Bullet] = []
        for en in self.enemies:
            if en.alive:
                en.update(pl.x, pl.y, self.walls, new_bullets, t, self.wave)
                # Contact damage
                if math.hypot(en.x-pl.x, en.y-pl.y) < en.r + pl.r:
                    pl.take_hit(en.contact_dmg)
                    self._burst(pl.x, pl.y, t["particle_hit"], 8)
        self.bullets.extend(new_bullets)

        # Update bullets
        for b in self.bullets:
            if not b.alive: continue
            b.update()
            bx = b.x; by = b.y
            # Out of map
            if bx < 0 or bx > self.map_w or by < 0 or by > self.map_h:
                b.alive = False; continue
            # Wall hit
            hit_wall = False
            for (wxx, wyy, www, whh) in self.walls:
                if wxx < bx < wxx+www and wyy < by < wyy+whh:
                    b.alive = False; hit_wall = True
                    self._burst(bx, by, t["particle_hit"], 4)
                    break
            if hit_wall: continue
            # Hit enemies / player
            if b.is_player:
                for en in self.enemies:
                    if not en.alive: continue
                    if math.hypot(en.x-bx, en.y-by) < en.r + b.r:
                        en.take_hit(b.dmg)
                        b.alive = False
                        self._burst(bx, by, t["particle_hit"], 10)
                        if not en.alive:
                            self._on_enemy_killed(en)
                        break
            else:
                if math.hypot(pl.x-bx, pl.y-by) < pl.r + b.r:
                    pl.take_hit(b.dmg)
                    b.alive = False
                    self._burst(bx, by, t["particle_hit"], 8)

        # Pickups
        for pk in self.pickups:
            if not pk.alive: continue
            pk.update()
            if math.hypot(pk.x-pl.x, pk.y-pl.y) < pk.r + pl.r:
                pk.alive = False
                if pk.kind == "hp":
                    pl.hp = min(pl.max_hp, pl.hp + pk.value)
                elif pk.kind == "ammo":
                    for w2 in pl.weapons:
                        w2["cur_ammo"] = min(w2["mag"], w2["cur_ammo"] + 15)
                elif pk.kind == "xp":
                    pl.xp += pk.value
                elif pk.kind == "weapon":
                    pl.weapon_idx = (pl.weapon_idx + 1) % len(pl.weapons)
                self._burst(pk.x, pk.y, t["pickup_xp"], 12)

        # Cleanup
        self.bullets  = [b for b in self.bullets  if b.alive]
        self.enemies  = [e for e in self.enemies  if e.alive]
        self.pickups  = [pk for pk in self.pickups if pk.alive]

        # Wave complete?
        if not self.spawn_queue and not self.enemies:
            self.wave_timer += 1
            if self.wave_timer >= FPS * 2:
                self.wave_timer = 0
                self._start_wave()

        # Particles
        for pt in self.particles:
            pt.update()
        self.particles = [pt for pt in self.particles if pt.life > 0]

        # Camera
        target_cx = pl.x - self.width() / 2
        target_cy = pl.y - self.height() / 2
        target_cx = max(0, min(target_cx, self.map_w - self.width()))
        target_cy = max(0, min(target_cy, self.map_h - self.height()))
        self.camera_x += (target_cx - self.camera_x) * 0.12
        self.camera_y += (target_cy - self.camera_y) * 0.12

        # Emit signals
        self.sig_score.emit(pl.score)
        self.sig_kills.emit(pl.kills)
        self.sig_hp.emit(pl.hp, pl.max_hp)
        w2 = pl.weapon
        self.sig_ammo.emit(w2["cur_ammo"], w2["mag"])
        self.sig_level.emit(pl.level)
        self.sig_xp.emit(pl.xp, pl.xp_next)
        self.sig_weapon.emit(w2["name"])

        if not pl.alive:
            self._die()
            return

        self.update()

    def _on_enemy_killed(self, en: Enemy):
        pl = self.player
        pl.score += en.score_val * self.wave
        pl.kills += 1
        pl.xp += en.score_val // 2
        self._burst(en.x, en.y, self.theme["particle_death"], 20)
        # Drop pickups
        if random.random() < 0.3:
            kind = random.choice(["hp","ammo","xp"])
            self.pickups.append(Pickup(en.x + random.uniform(-20,20),
                                       en.y + random.uniform(-20,20), kind))
        if random.random() < 0.05:
            self.pickups.append(Pickup(en.x, en.y, "weapon"))

    def _burst(self, x, y, color, count):
        for _ in range(count):
            self.particles.append(Particle(x, y, color))

    def _die(self):
        self.state = "dead"
        self.timer.stop()
        sc = self.player.score
        if sc > self.best:
            self.best = sc
        self.sig_dead.emit(sc, self.best)
        self.sig_best.emit(self.best)
        self._burst(self.player.x, self.player.y,
                    self.theme["particle_death"], 50)
        self.update()

    def keyPressEvent(self, e):
        self.keys_held.add(e.key())
        if self.state == "playing":
            k = e.key()
            if k == Qt.Key.Key_R:
                self.player.reload()
            elif k == Qt.Key.Key_1:
                self.player.weapon_idx = 0
                self.sig_weapon.emit(self.player.weapon["name"])
            elif k == Qt.Key.Key_2:
                self.player.weapon_idx = 1
                self.sig_weapon.emit(self.player.weapon["name"])
            elif k == Qt.Key.Key_3:
                self.player.weapon_idx = 2
                self.sig_weapon.emit(self.player.weapon["name"])
            elif k == Qt.Key.Key_Escape:
                self.pause_toggle()
        elif self.state == "paused":
            if e.key() == Qt.Key.Key_Escape:
                self.pause_toggle()

    def keyReleaseEvent(self, e):
        self.keys_held.discard(e.key())

    def mouseMoveEvent(self, e):
        self.mouse_x = e.position().x()
        self.mouse_y = e.position().y()

    def mousePressEvent(self, e):
        self.setFocus()
        if e.button() == Qt.MouseButton.LeftButton:
            self.mouse_down = True
            if self.state == "playing":
                pl = self.player
                wx = self.mouse_x + self.camera_x
                wy = self.mouse_y + self.camera_y
                pl.try_shoot(wx, wy, self.bullets, self.particles, self.theme)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.mouse_down = False

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        t = self.theme

        p.save()
        p.translate(-self.camera_x, -self.camera_y)

        self._draw_floor(p, t)
        self._draw_walls(p, t)
        for pk in self.pickups:
            pk.draw(p, t)
        for b in self.bullets:
            b.draw(p, t)
        for en in self.enemies:
            en.draw(p, t)
        if self.player:
            self.player.draw(p, t)
        for pt in self.particles:
            pt.draw(p)

        p.restore()

        self._draw_hud(p, t)
        self._draw_crosshair(p, t)
        if self.state in ("dead", "idle", "paused"):
            self._draw_overlay(p, t)

    def _draw_floor(self, p: QPainter, t: dict):
        cx0 = int(self.camera_x // TILE) * TILE
        cy0 = int(self.camera_y // TILE) * TILE
        cx1 = cx0 + self.width() + TILE * 2
        cy1 = cy0 + self.height() + TILE * 2

        for (fx, fy, fw, fh) in self.floor_tiles:
            if fx + fw < cx0 or fx > cx1 or fy + fh < cy0 or fy > cy1:
                continue
            col = ((fx//TILE) + (fy//TILE)) % 2
            c = QColor(t["floor"] if col == 0 else t["floor2"])
            p.fillRect(QRectF(fx, fy, fw, fh), c)
            lc = QColor(t["floor_line"])
            p.setPen(QPen(lc, 0.5))
            p.drawRect(QRectF(fx, fy, fw, fh))

    def _draw_walls(self, p: QPainter, t: dict):
        for (wx, wy, ww, wh) in self.walls:
            grad = QLinearGradient(wx, wy, wx+ww, wy+wh)
            grad.setColorAt(0, QColor(t["wall"]).lighter(130))
            grad.setColorAt(1, QColor(t["wall"]))
            p.setBrush(QBrush(grad))
            p.setPen(QPen(QColor(t["wall_border"]), 1.5))
            p.drawRect(QRectF(wx, wy, ww, wh))

    def _draw_hud(self, p: QPainter, t: dict):
        if self.state not in ("playing", "paused") or not self.player:
            return
        pl = self.player
        W = self.width()

        # Top bar background
        hc = QColor(t["hud_bg"])
        p.fillRect(QRectF(0, 0, W, 54), hc)

        # HP bar
        bar_w = min(160, W // 5)
        self._draw_bar(p, 10, 10, bar_w, 14,
                       pl.hp / pl.max_hp, t["hp_bar"], t["hp_bar2"])
        p.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        p.setPen(QPen(QColor(t["hud_text"])))
        p.drawText(QRectF(10, 26, bar_w, 16),
                   Qt.AlignmentFlag.AlignLeft, f"HP {pl.hp}/{pl.max_hp}")

        # Ammo bar
        w2 = pl.weapon
        reloading = w2["reload_timer"] > 0
        bar_x2 = 20 + bar_w
        self._draw_bar(p, bar_x2, 10, bar_w, 14,
                       w2["cur_ammo"]/w2["mag"] if not reloading else
                       1 - w2["reload_timer"]/(w2["reload"]*3),
                       t["ammo_bar"] if not reloading else "#AAAAAA",
                       t["hp_bar2"])
        reload_txt = "RELOADING..." if reloading else f"{w2['cur_ammo']}/{w2['mag']}"
        p.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        p.setPen(QPen(QColor(t["ammo_bar"])))
        p.drawText(QRectF(bar_x2, 26, bar_w, 16),
                   Qt.AlignmentFlag.AlignLeft, reload_txt)

        # XP bar
        bar_x3 = 30 + bar_w * 2
        self._draw_bar(p, bar_x3, 10, bar_w, 14,
                       pl.xp / pl.xp_next, t["xp_bar"], t["hp_bar2"])
        p.setPen(QPen(QColor(t["xp_bar"])))
        p.drawText(QRectF(bar_x3, 26, bar_w, 16),
                   Qt.AlignmentFlag.AlignLeft,
                   f"LVL {pl.level}  XP {pl.xp}/{pl.xp_next}")

        # Score / Wave / Kills on right
        p.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        p.setPen(QPen(QColor(t["accent"])))
        p.drawText(QRectF(W-220, 6, 210, 22),
                   Qt.AlignmentFlag.AlignRight,
                   f"⭐ {pl.score}   Wave {self.wave}")
        p.setFont(QFont("Arial", 9))
        p.setPen(QPen(QColor(t["text2"])))
        p.drawText(QRectF(W-220, 28, 210, 18),
                   Qt.AlignmentFlag.AlignRight,
                   f"Kills {pl.kills}   {w2['name']}   FPS {self._fps_val}")

        # Wave progress mini-bar
        if self.enemies_this_wave > 0:
            prog = 1 - (len(self.enemies) + len(self.spawn_queue)) / self.enemies_this_wave
            prog = max(0.0, min(1.0, prog))
            self._draw_bar(p, W//2 - 80, 36, 160, 10,
                           prog, t["xp_bar"], t["hp_bar2"])

    def _draw_bar(self, p, x, y, w, h, ratio, col, bg_col):
        p.setBrush(QBrush(QColor(bg_col))); p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(QRectF(x, y, w, h), 3, 3)
        if ratio > 0:
            grad = QLinearGradient(x, y, x+w, y)
            grad.setColorAt(0, QColor(col).lighter(150))
            grad.setColorAt(1, QColor(col))
            p.setBrush(QBrush(grad))
            p.drawRoundedRect(QRectF(x, y, w * ratio, h), 3, 3)

    def _draw_crosshair(self, p: QPainter, t: dict):
        if self.state != "playing":
            return
        mx = self.mouse_x; my = self.mouse_y
        c = QColor(t["crosshair"])
        p.setPen(QPen(c, 2))
        size = 10; gap = 4
        p.drawLine(QPointF(mx-size-gap, my), QPointF(mx-gap, my))
        p.drawLine(QPointF(mx+gap, my),    QPointF(mx+size+gap, my))
        p.drawLine(QPointF(mx, my-size-gap), QPointF(mx, my-gap))
        p.drawLine(QPointF(mx, my+gap),    QPointF(mx, my+size+gap))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawEllipse(QRectF(mx-4, my-4, 8, 8))

    def _draw_overlay(self, p: QPainter, t: dict):
        oc = QColor(t["overlay_bg"])
        p.fillRect(self.rect(), oc)
        W = self.width(); H = self.height()

        if self.state == "idle":
            self._ctext(p, t["text"], "▶  Click START or press SPACE", 28, bold=True, y=H//2-20)

        elif self.state == "paused":
            self._ctext(p, t["accent"], "⏸  PAUSED", 46, bold=True, y=H//2-40)
            self._ctext(p, t["text2"], "ESC to Resume", 18, y=H//2+20)

        elif self.state == "dead":
            self._ctext(p, t["accent"], "GAME OVER", 52, bold=True, y=H//2-60)
            if self.player:
                self._ctext(p, t["text"],
                            f"Score: {self.player.score}   Wave: {self.wave}   Kills: {self.player.kills}",
                            20, y=H//2)
            if self.player and self.player.score >= self.best and self.best > 0:
                self._ctext(p, "#FFD700", "🏆  NEW BEST!", 24, bold=True, y=H//2+40)
            self._ctext(p, t["text2"], "Click RESTART to play again", 16, y=H//2+75)

    def _ctext(self, p: QPainter, color: str, text: str, size: int,
               bold=False, y=None):
        W = self.width(); H = self.height()
        p.setFont(QFont("Arial", size,
                        QFont.Weight.Bold if bold else QFont.Weight.Normal))
        p.setPen(QPen(QColor(color)))
        yy = y if y is not None else H // 2
        p.drawText(QRectF(0, yy, W, size + 12),
                   Qt.AlignmentFlag.AlignHCenter, text)


# ───────────────────────────────────────────────────────────────────────────────
# STYLED BUTTON HELPER
# ───────────────────────────────────────────────────────────────────────────────
def make_button(text: str, bg: str, hover: str, txt: str) -> QPushButton:
    btn = QPushButton(text)
    btn.setCursor(Qt.CursorShape.PointingHandCursor)
    btn.setMinimumHeight(36)
    btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    btn.setStyleSheet(f"""
        QPushButton {{
            background: {bg}; color: {txt};
            border: none; border-radius: 7px;
            font-size: 13px; font-weight: bold;
            padding: 6px 10px;
        }}
        QPushButton:hover {{ background: {hover}; }}
        QPushButton:pressed {{ background: {hover}; opacity: 0.8; }}
    """)
    return btn


# ───────────────────────────────────────────────────────────────────────────────
# MAIN WINDOW
# ───────────────────────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang = "en"
        self.theme_key = "dark"
        self.theme = THEMES[self.theme_key]
        self.setWindowTitle(TR[self.lang]["title"])
        self.setMinimumSize(640, 400)
        self.resize(1080, 660)

        self._build_ui()
        self._apply_theme()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Game Widget ──
        self.game = GameWidget(self.theme)
        self.game.sig_score.connect(self._on_score)
        self.game.sig_best.connect(self._on_best)
        self.game.sig_wave.connect(self._on_wave)
        self.game.sig_kills.connect(self._on_kills)
        self.game.sig_hp.connect(self._on_hp)
        self.game.sig_ammo.connect(self._on_ammo)
        self.game.sig_level.connect(self._on_level)
        self.game.sig_xp.connect(self._on_xp)
        self.game.sig_weapon.connect(self._on_weapon)
        self.game.sig_dead.connect(self._on_dead)
        self.game.sig_attempts.connect(self._on_attempts)
        self.game.sig_fps.connect(self._on_fps)
        root.addWidget(self.game, stretch=1)

        # ── Side Panel ──
        self.panel = QFrame()
        self.panel.setFixedWidth(210)
        self.panel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        panel_layout = QVBoxLayout(self.panel)
        panel_layout.setContentsMargins(10, 14, 10, 14)
        panel_layout.setSpacing(8)
        root.addWidget(self.panel)

        t = self.theme
        tr = TR[self.lang]

        # Title
        self.lbl_title = QLabel(tr["title"])
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.lbl_title.setWordWrap(True)
        panel_layout.addWidget(self.lbl_title)
        panel_layout.addSpacing(4)

        # Stats grid
        stats_frame = QFrame()
        stats_grid = QGridLayout(stats_frame)
        stats_grid.setContentsMargins(6, 6, 6, 6)
        stats_grid.setSpacing(4)

        def stat_pair(label_key, val_default):
            lbl = QLabel(TR[self.lang][label_key])
            lbl.setFont(QFont("Arial", 9))
            val = QLabel(val_default)
            val.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            val.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            return lbl, val

        self.lbl_score_key, self.lbl_score = stat_pair("score", "0")
        self.lbl_best_key,  self.lbl_best  = stat_pair("best",  "0")
        self.lbl_wave_key,  self.lbl_wave  = stat_pair("wave",  "—")
        self.lbl_kills_key, self.lbl_kills = stat_pair("kills", "0")
        self.lbl_hp_key,    self.lbl_hp    = stat_pair("hp",    "100/100")
        self.lbl_ammo_key,  self.lbl_ammo  = stat_pair("ammo",  "—")
        self.lbl_level_key, self.lbl_level = stat_pair("level", "1")
        self.lbl_xp_key,    self.lbl_xp    = stat_pair("xp",    "0/100")
        self.lbl_weapon_key,self.lbl_weapon= stat_pair("weapon","Pistol")
        self.lbl_runs_key,  self.lbl_runs  = stat_pair("attempts", "0")
        self.lbl_fps_key,   self.lbl_fps   = stat_pair("fps",  "0")

        pairs = [
            (self.lbl_score_key,  self.lbl_score),
            (self.lbl_best_key,   self.lbl_best),
            (self.lbl_wave_key,   self.lbl_wave),
            (self.lbl_kills_key,  self.lbl_kills),
            (self.lbl_hp_key,     self.lbl_hp),
            (self.lbl_ammo_key,   self.lbl_ammo),
            (self.lbl_level_key,  self.lbl_level),
            (self.lbl_xp_key,     self.lbl_xp),
            (self.lbl_weapon_key, self.lbl_weapon),
            (self.lbl_runs_key,   self.lbl_runs),
            (self.lbl_fps_key,    self.lbl_fps),
        ]
        for i, (k, v) in enumerate(pairs):
            stats_grid.addWidget(k, i, 0)
            stats_grid.addWidget(v, i, 1)
        panel_layout.addWidget(stats_frame)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        panel_layout.addWidget(sep)

        # Buttons
        self.btn_start = make_button(tr["start"], t["btn_bg"], t["btn_h"], t["btn_txt"])
        self.btn_pause = make_button(tr["pause"], t["btn2_bg"], t["btn2_h"], t["btn_txt"])
        self.btn_restart = make_button(tr["restart"], t["btn3_bg"], t["btn3_h"], t["btn_txt"])
        self.btn_start.clicked.connect(self._on_start)
        self.btn_pause.clicked.connect(self._on_pause)
        self.btn_restart.clicked.connect(self._on_restart)
        panel_layout.addWidget(self.btn_start)
        panel_layout.addWidget(self.btn_pause)
        panel_layout.addWidget(self.btn_restart)

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        panel_layout.addWidget(sep2)

        # Theme selector
        theme_row = QHBoxLayout()
        self.lbl_theme = QLabel(tr["theme"])
        self.lbl_theme.setFont(QFont("Arial", 9))
        self.cmb_theme = QComboBox()
        self.cmb_theme.addItems([tr["dark"], tr["light"]])
        self.cmb_theme.setCurrentIndex(0)
        self.cmb_theme.currentIndexChanged.connect(self._on_theme_change)
        theme_row.addWidget(self.lbl_theme)
        theme_row.addWidget(self.cmb_theme)
        panel_layout.addLayout(theme_row)

        # Language selector
        lang_row = QHBoxLayout()
        self.lbl_lang = QLabel(tr["language"])
        self.lbl_lang.setFont(QFont("Arial", 9))
        self.cmb_lang = QComboBox()
        self.cmb_lang.addItems(["English", "中文", "فارسی"])
        self.cmb_lang.setCurrentIndex(0)
        self.cmb_lang.currentIndexChanged.connect(self._on_lang_change)
        lang_row.addWidget(self.lbl_lang)
        lang_row.addWidget(self.cmb_lang)
        panel_layout.addLayout(lang_row)

        sep3 = QFrame()
        sep3.setFrameShape(QFrame.Shape.HLine)
        panel_layout.addWidget(sep3)

        # Controls hint
        self.lbl_controls = QLabel(tr["controls"])
        self.lbl_controls.setWordWrap(True)
        self.lbl_controls.setFont(QFont("Arial", 8))
        self.lbl_controls.setAlignment(Qt.AlignmentFlag.AlignCenter)
        panel_layout.addWidget(self.lbl_controls)

        panel_layout.addStretch()

        self._stat_labels = [
            (self.lbl_score_key,  "score"),
            (self.lbl_best_key,   "best"),
            (self.lbl_wave_key,   "wave"),
            (self.lbl_kills_key,  "kills"),
            (self.lbl_hp_key,     "hp"),
            (self.lbl_ammo_key,   "ammo"),
            (self.lbl_level_key,  "level"),
            (self.lbl_xp_key,     "xp"),
            (self.lbl_weapon_key, "weapon"),
            (self.lbl_runs_key,   "attempts"),
            (self.lbl_fps_key,    "fps"),
        ]

    # ── Signal handlers ──────────────────────────────────────────────────────
    def _on_score(self, v):   self.lbl_score.setText(str(v))
    def _on_best(self, v):    self.lbl_best.setText(str(v))
    def _on_wave(self, v):    self.lbl_wave.setText(str(v))
    def _on_kills(self, v):   self.lbl_kills.setText(str(v))
    def _on_hp(self, cur, mx):self.lbl_hp.setText(f"{cur}/{mx}")
    def _on_ammo(self, cur, mx): self.lbl_ammo.setText(f"{cur}/{mx}")
    def _on_level(self, v):   self.lbl_level.setText(str(v))
    def _on_xp(self, cur, nx):self.lbl_xp.setText(f"{cur}/{nx}")
    def _on_weapon(self, n):  self.lbl_weapon.setText(n)
    def _on_attempts(self, v):self.lbl_runs.setText(str(v))
    def _on_fps(self, v):     self.lbl_fps.setText(str(v))
    def _on_dead(self, sc, best):
        self.lbl_score.setText(str(sc))
        self.lbl_best.setText(str(best))
        self.btn_start.hide()
        self.btn_pause.hide()
        self.btn_restart.show()

    # ── Button actions ────────────────────────────────────────────────────────
    def _on_start(self):
        self.game.start()
        self.btn_start.hide()
        self.btn_restart.show()
        self.btn_pause.show()
        tr = TR[self.lang]
        self.btn_pause.setText(tr["pause"])

    def _on_pause(self):
        self.game.pause_toggle()
        tr = TR[self.lang]
        if self.game.state == "paused":
            self.btn_pause.setText(tr["resume"])
        else:
            self.btn_pause.setText(tr["pause"])

    def _on_restart(self):
        self.game.start()
        self.btn_start.hide()
        self.btn_restart.show()
        self.btn_pause.show()
        tr = TR[self.lang]
        self.btn_pause.setText(tr["pause"])

    # ── Theme / Language ──────────────────────────────────────────────────────
    def _on_theme_change(self, idx):
        self.theme_key = "dark" if idx == 0 else "light"
        self.theme = THEMES[self.theme_key]
        self.game.set_theme(self.theme)
        self._apply_theme()

    def _on_lang_change(self, idx):
        self.lang = ["en", "zh", "fa"][idx]
        self._retranslate()
        self._apply_theme()

    def _apply_theme(self):
        t = self.theme
        tr = TR[self.lang]

        self.setStyleSheet(f"QMainWindow {{ background: {t['win_bg']}; }}")
        self.panel.setStyleSheet(f"""
            QFrame {{
                background: {t['panel_bg']};
                border-left: 1px solid {t['panel_border']};
            }}
            QLabel {{ color: {t['text']}; background: transparent; border: none; }}
            QFrame[frameShape="4"] {{ background: {t['panel_border']}; border: none; max-height: 1px; }}
        """)
        cmb_style = f"""
            QComboBox {{
                background: {t['cmb_bg']}; color: {t['text']};
                border: 1px solid {t['cmb_border']}; border-radius: 5px;
                padding: 3px 6px; font-size: 11px;
            }}
            QComboBox::drop-down {{ border: none; }}
            QComboBox QAbstractItemView {{
                background: {t['cmb_bg']}; color: {t['text']};
                selection-background-color: {t['btn_h']};
            }}
        """
        self.cmb_theme.setStyleSheet(cmb_style)
        self.cmb_lang.setStyleSheet(cmb_style)

        for lbl in [self.lbl_score, self.lbl_best, self.lbl_wave, self.lbl_kills]:
            lbl.setStyleSheet(f"color: {t['accent']}; font-weight: bold;")
        self.lbl_hp.setStyleSheet(f"color: {t['hp_bar']};")
        self.lbl_ammo.setStyleSheet(f"color: {t['ammo_bar']};")
        self.lbl_xp.setStyleSheet(f"color: {t['xp_bar']};")
        self.lbl_level.setStyleSheet(f"color: {t['xp_bar']}; font-weight: bold;")
        self.lbl_controls.setStyleSheet(f"color: {t['text2']};")
        self.lbl_title.setStyleSheet(f"color: {t['accent']};")

        self.btn_start.setStyleSheet(f"""
            QPushButton {{ background: {t['btn_bg']}; color: {t['btn_txt']};
                border: none; border-radius: 7px; font-size: 13px;
                font-weight: bold; padding: 7px 10px; }}
            QPushButton:hover {{ background: {t['btn_h']}; }}
        """)
        self.btn_pause.setStyleSheet(f"""
            QPushButton {{ background: {t['btn2_bg']}; color: {t['btn_txt']};
                border: none; border-radius: 7px; font-size: 13px;
                font-weight: bold; padding: 7px 10px; }}
            QPushButton:hover {{ background: {t['btn2_h']}; }}
        """)
        self.btn_restart.setStyleSheet(f"""
            QPushButton {{ background: {t['btn3_bg']}; color: {t['btn_txt']};
                border: none; border-radius: 7px; font-size: 13px;
                font-weight: bold; padding: 7px 10px; }}
            QPushButton:hover {{ background: {t['btn3_h']}; }}
        """)

    def _retranslate(self):
        tr = TR[self.lang]
        self.setWindowTitle(tr["title"])
        self.lbl_title.setText(tr["title"])
        is_rtl = self.lang == "fa"
        self.panel.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft if is_rtl
            else Qt.LayoutDirection.LeftToRight)

        for lbl, key in self._stat_labels:
            lbl.setText(tr[key])

        self.lbl_theme.setText(tr["theme"])
        self.lbl_lang.setText(tr["language"])
        self.lbl_controls.setText(tr["controls"])

        s = self.game.state
        self.btn_start.setText(tr["start"])
        self.btn_restart.setText(tr["restart"])
        self.btn_pause.setText(tr["pause"] if s != "paused" else tr["resume"])

        # Theme combobox items
        self.cmb_theme.blockSignals(True)
        self.cmb_theme.setItemText(0, tr["dark"])
        self.cmb_theme.setItemText(1, tr["light"])
        self.cmb_theme.blockSignals(False)

        # Visibility based on state
        if s == "idle":
            self.btn_start.show()
            self.btn_pause.hide()
            self.btn_restart.hide()
        elif s in ("playing", "paused"):
            self.btn_start.hide()
            self.btn_pause.show()
            self.btn_restart.show()
        else:
            self.btn_start.hide()
            self.btn_pause.hide()
            self.btn_restart.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Space and self.game.state == "idle":
            self._on_start()
        else:
            self.game.keyPressEvent(e)

    def keyReleaseEvent(self, e):
        self.game.keyReleaseEvent(e)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.game.update()


# ───────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ───────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Nuclear Throne 2D")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
