from flask import Flask
from dnd_api_personagens.extensions import db
from dnd_api_personagens.models.equipamento import Equipamento, Arma
from .magia import Magia
from .personagem import Personagem
import os

