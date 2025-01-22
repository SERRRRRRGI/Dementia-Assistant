import SwiftUI

struct ContentView: View {
    @State private var isRecording = false

    var body: some View {
        VStack(spacing: 20) {
            Text("Audio Recorder")
                .font(.largeTitle)
                .bold()

            Button(action: {
                if !isRecording {
                    // Request microphone permission before starting
                    AudioRecorder.shared.requestMicrophonePermission { granted in
                        if granted {
                            AudioRecorder.shared.startRecording()
                            isRecording = true
                        } else {
                            print("Microphone permission denied.")
                        }
                    }
                } else {
                    // Stop recording
                    AudioRecorder.shared.stopRecording()
                    isRecording = false
                }
            }) {
                Text(isRecording ? "Stop Recording" : "Start Recording")
                    .foregroundColor(.white)
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(isRecording ? Color.red : Color.green)
                    .cornerRadius(10)
            }
            .padding(.horizontal)
        }
        .padding()
    }
}
