
from playwright.sync_api import Page, expect


def test_todomvc(page: Page):

    # 1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/")

    # 2. Adicionar uma tarefa
    campo = page.locator(".new-todo")
    campo.fill("Estudar QA Automation")
    campo.press("Enter")

    # Verificar se a tarefa apareceu
    tarefa = page.locator(".todo-list li")
    expect(tarefa).to_have_text("Estudar QA Automation")

    # 3. Marcar como concluida
    tarefa.locator(".toggle").check()
    expect(tarefa).to_have_class("completed")

    # 4. Atualizar a pagina
    page.reload()

    # 5. Verificar se a tarefa continua salva
    tarefa = page.locator(".todo-list li")
    expect(tarefa).to_have_text("Estudar QA Automation")
    expect(tarefa).to_have_class("completed")


def test_duas_tarefas(page: Page):

    # 1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/")

    # 2. Adicionar duas tarefas
    campo = page.locator(".new-todo")
    campo.fill("Estudar Python")
    campo.press("Enter")

    campo.fill("Estudar Playwright")
    campo.press("Enter")

    # Verificar se apareceram 2 tarefas
    tarefa = page.locator(".todo-list li")
    expect(tarefa).to_have_count(2)

    # 3. Marcar como concluidas
    tarefa.nth(0).locator(".toggle").check()
    tarefa.nth(1).locator(".toggle").check()
    expect(tarefa).to_have_class(["completed", "completed"])

    # 4. Atualizar pagina
    page.reload()

    # 5. Verificar se as tarefas continuam salvas
    tarefa = page.locator(".todo-list li")
    expect(tarefa).to_have_text([
        "Estudar Python",
        "Estudar Playwright"
    ])
    expect(tarefa).to_have_class(["completed", "completed"])


def test_excluir_tarefa(page: Page):

    # Missao 04: excluir uma tarefa

    # 1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/")

    # 2. Criar tarefas
    campo = page.locator(".new-todo")

    campo.fill("verde")
    campo.press("Enter")

    campo.fill("amarelo")
    campo.press("Enter")

    # 3. Excluir a primeira tarefa
    tarefa = page.locator(".todo-list li")
    tarefa.nth(0).hover()
    tarefa.nth(0).locator(".destroy").click()

    # 4. Verificar se excluiu a tarefa
    expect(tarefa).to_have_count(1)
    expect(tarefa).to_have_text("amarelo")

def test_marcar_desmarcar(page: page):
   #Missão 05

    #1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/#/")

    #2. Criatarefas
    campo = page.locator(".new-todo")
    campo.fill("Estudar python")
    campo.press("Enter")

    #3. Marcar tarefa como concluída
    tarefa = page.locator(".todo-list li")
    tarefa.nth(0).hover()
    tarefa.nth(0).locator(".toggle").click()

    #4. Verificar se tarefa está marcada como concluída
    expect(tarefa).to_have_text("Estudar python")
    expect(tarefa).to_have_class("completed")


def test_tarefa_vazia(page: page):
   
    #1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/#/")

    #2. Criar tarefa vazia
    campo = page.locator(".new-todo")
    campo.fill(" ")
    campo.press("Enter")

    #3. Verificar se lista permance vazia
    tarefa = page.locator(".todo-list li")
    expect(tarefa).to_have_count(0)


def test_filtro_active(page: Page):
    # Missao 07

    # 1. Abrir o site
    page.goto("https://demo.playwright.dev/todomvc/#/")
    
    # 2. Criar tarefas
    campo = page.locator(".new-todo")
    campo.fill("Estudar Python")
    campo.press("Enter")
    campo.fill("Estudar Playwright")
    campo.press("Enter")
    campo.fill("Estudar QA")
    campo.press("Enter")

    # 3. Marcar a primeira tarefa
    tarefa = page.locator(".todo-list li")
    tarefa.nth(0).locator(".toggle").check()

    # 4. Clicar no filtro Active
    page.locator('a[href="#/active"]').click()

    # 5. Verificar se duas tarefas permanecem
    active = page.locator(".todo-list li")
    expect(active).to_have_count(2)
    expect(active).to_have_text([
        "Estudar Playwright",
        "Estudar QA"
    ])







   