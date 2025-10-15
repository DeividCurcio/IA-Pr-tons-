#!/usr/bin/env python3
"""
Robocop Policial - Sistema de Segurança Inteligente
Um sistema de IA para monitoramento e detecção de ameaças
"""

import random
import time
from datetime import datetime
from enum import Enum


class NivelAmeaca(Enum):
    """Níveis de ameaça detectáveis pelo sistema"""
    BAIXO = 1
    MEDIO = 2
    ALTO = 3
    CRITICO = 4


class RobocopPolicial:
    """
    Sistema Robocop Policial - IA para segurança e proteção
    """
    
    def __init__(self, nome="ROBOCOP-001", area_patrulha="Centro"):
        self.nome = nome
        self.area_patrulha = area_patrulha
        self.ativo = False
        self.incidentes_detectados = []
        self.patrulhas_realizadas = 0
        
    def ativar(self):
        """Ativa o sistema Robocop"""
        self.ativo = True
        print(f"[{self.timestamp()}] {self.nome} ATIVADO")
        print(f"Área de patrulha: {self.area_patrulha}")
        print("Sistema de segurança iniciado...")
        
    def desativar(self):
        """Desativa o sistema Robocop"""
        self.ativo = False
        print(f"[{self.timestamp()}] {self.nome} DESATIVADO")
        print(f"Total de patrulhas: {self.patrulhas_realizadas}")
        print(f"Incidentes detectados: {len(self.incidentes_detectados)}")
        
    @staticmethod
    def timestamp():
        """Retorna timestamp atual"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def analisar_ambiente(self):
        """Analisa o ambiente em busca de ameaças"""
        if not self.ativo:
            print("Sistema desativado. Ative primeiro.")
            return None
            
        # Simula análise do ambiente
        nivel = random.choice(list(NivelAmeaca))
        
        if nivel == NivelAmeaca.BAIXO:
            situacao = "Área segura"
            acao = "Continuar patrulha normal"
        elif nivel == NivelAmeaca.MEDIO:
            situacao = "Atividade suspeita detectada"
            acao = "Aumentar vigilância"
        elif nivel == NivelAmeaca.ALTO:
            situacao = "Possível ameaça identificada"
            acao = "Solicitar reforços"
        else:  # CRITICO
            situacao = "AMEAÇA IMINENTE DETECTADA"
            acao = "INTERVIR IMEDIATAMENTE"
            
        return {
            'nivel': nivel,
            'situacao': situacao,
            'acao': acao,
            'timestamp': self.timestamp()
        }
    
    def executar_patrulha(self):
        """Executa uma patrulha na área designada"""
        if not self.ativo:
            print("Sistema desativado. Ative primeiro.")
            return
            
        self.patrulhas_realizadas += 1
        print(f"\n{'='*60}")
        print(f"PATRULHA #{self.patrulhas_realizadas}")
        print(f"Área: {self.area_patrulha}")
        print(f"{'='*60}")
        
        # Analisa ambiente
        resultado = self.analisar_ambiente()
        
        print(f"Timestamp: {resultado['timestamp']}")
        print(f"Nível de ameaça: {resultado['nivel'].name}")
        print(f"Situação: {resultado['situacao']}")
        print(f"Ação recomendada: {resultado['acao']}")
        
        # Registra incidente se necessário
        if resultado['nivel'].value >= NivelAmeaca.MEDIO.value:
            self.incidentes_detectados.append(resultado)
            print(f"⚠️  INCIDENTE REGISTRADO (Total: {len(self.incidentes_detectados)})")
        
        return resultado
    
    def relatorio_incidentes(self):
        """Gera relatório dos incidentes detectados"""
        print(f"\n{'='*60}")
        print(f"RELATÓRIO DE INCIDENTES - {self.nome}")
        print(f"{'='*60}")
        print(f"Área de patrulha: {self.area_patrulha}")
        print(f"Total de patrulhas: {self.patrulhas_realizadas}")
        print(f"Incidentes detectados: {len(self.incidentes_detectados)}\n")
        
        if not self.incidentes_detectados:
            print("Nenhum incidente registrado.")
        else:
            for i, incidente in enumerate(self.incidentes_detectados, 1):
                print(f"Incidente #{i}:")
                print(f"  Timestamp: {incidente['timestamp']}")
                print(f"  Nível: {incidente['nivel'].name}")
                print(f"  Situação: {incidente['situacao']}")
                print(f"  Ação: {incidente['acao']}")
                print()


def main():
    """Função principal - demonstração do sistema"""
    print("="*60)
    print("SISTEMA ROBOCOP POLICIAL")
    print("IA de Segurança e Proteção")
    print("="*60)
    print()
    
    # Criar instância do Robocop
    robocop = RobocopPolicial(nome="ROBOCOP-001", area_patrulha="Centro da Cidade")
    
    # Ativar sistema
    robocop.ativar()
    print()
    
    # Executar patrulhas
    num_patrulhas = 5
    for i in range(num_patrulhas):
        robocop.executar_patrulha()
        if i < num_patrulhas - 1:
            time.sleep(1)  # Pausa entre patrulhas
    
    # Gerar relatório
    print()
    robocop.relatorio_incidentes()
    
    # Desativar sistema
    print()
    robocop.desativar()


if __name__ == "__main__":
    main()
