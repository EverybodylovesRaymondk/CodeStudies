package com.codebind;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class App {
    private JButton okButton;
    private JPanel pannelMain;
    private JFormattedTextField enterNameHereFormattedTextField;

    public App() {
        okButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null,"Hello World");
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame=new JFrame("App");
        frame.setContentPane(new App().pannelMain);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);

    }
}