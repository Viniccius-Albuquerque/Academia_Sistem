let ultimoAlunoConsultado = null;

$("#form-treino").addEventListener("submit", async evento => {
    evento.preventDefault();

    const treino = {
        nome: $("#treino-nome").value.trim(),
        dia_semana: $("#treino-dia").value,
        id_aluno: Number($("#treino-aluno").value)
    };

    try {
        await requisicao("/treino/", {
            method: "POST",
            body: JSON.stringify(treino)
        });

        $("#form-treino").reset();

        mostrarMensagem("Treino cadastrado com sucesso!");

        if (ultimoAlunoConsultado === treino.id_aluno) {
            await carregarTreinos(treino.id_aluno);
        }

    } catch (erro) {
        mostrarErro(erro);
    }
});

async function carregarTreinos(idAluno) {
    const tabela = $("#lista-treinos");

    ultimoAlunoConsultado = idAluno;

    tabela.innerHTML = `
        <tr>
            <td colspan="4" class="tabela-vazia">Carregando treinos...</td>
        </tr>
    `;

    try {
        const treinos = await requisicao(`/treino/${idAluno}`);

        tabela.innerHTML = "";

        if (treinos.length === 0) {
            tabela.innerHTML = `
                <tr>
                    <td colspan="4" class="tabela-vazia">
                        Este aluno ainda não possui treinos.
                    </td>
                </tr>
            `;
            return;
        }

        treinos.forEach(treino => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${escaparHTML(treino.id)}</td>
                <td>${escaparHTML(treino.nome)}</td>
                <td>${escaparHTML(formatarDia(treino.dia_semana))}</td>
                <td>${escaparHTML(treino.id_aluno)}</td>
            `;

            tabela.appendChild(linha);
        });

    } catch (erro) {
        tabela.innerHTML = `
            <tr>
                <td colspan="4" class="tabela-vazia">
                    Não foi possível carregar os treinos.
                </td>
            </tr>
        `;

        mostrarErro(erro);
    }
}

$("#buscar-treinos").addEventListener("submit", async evento => {
    evento.preventDefault();

    const idAluno = Number($("#buscar-treino-aluno").value);

    await carregarTreinos(idAluno);
});

$("#form-atualizar-treino").addEventListener("submit", async evento => {
    evento.preventDefault();

    const idAluno = Number($("#atualizar-treino-aluno").value);
    const dia_semana = $("#atualizar-treino-dia").value;
    const nome = $("#atualizar-treino-nome").value.trim();

    try {
        await requisicao(`/treino/${idAluno}`, {
            method: "PUT",
            body: JSON.stringify({
                nome,
                dia_semana
            })
        });

        mostrarMensagem("Treino atualizado com sucesso!");

        if (ultimoAlunoConsultado === idAluno) {
            await carregarTreinos(idAluno);
        }

    } catch (erro) {
        mostrarErro(erro);
    }
});

$("#form-excluir-treino").addEventListener("submit", async evento => {
    evento.preventDefault();

    const idAluno = Number($("#excluir-treino-aluno").value);
    const dia_semana = $("#excluir-treino-dia").value;

    const confirmacao = confirm(
        "Deseja realmente excluir o treino deste aluno nesse dia? Verifique também os exercícios associados."
    );

    if (!confirmacao) {
        return;
    }

    try {
        await requisicao("/treino/delete", {
            method: "DELETE",
            body: JSON.stringify({
                id_aluno: idAluno,
                dia_semana
            })
        });

        mostrarMensagem("Solicitação de exclusão do treino concluída!");

        if (ultimoAlunoConsultado === idAluno) {
            await carregarTreinos(idAluno);
        }

    } catch (erro) {
        mostrarErro(erro);
    }
});