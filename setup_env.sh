#!/bin/bash

# Obter o diretório onde o script está localizado
SCRIPT_DIR=$(dirname $(realpath $0))

# Diretório src do projeto
SRC_DIR="${SCRIPT_DIR}/flappyBirdMain"

# Configurar PYTHONPATH para incluir o diretório src do projeto
export PYTHONPATH="${SRC_DIR}:${PYTHONPATH}"

# Informar o usuário que o ambiente está configurado
echo "Ambiente configurado. PYTHONPATH: ${PYTHONPATH}"

# Executar o shell atual para manter as configurações
exec "$SHELL"
